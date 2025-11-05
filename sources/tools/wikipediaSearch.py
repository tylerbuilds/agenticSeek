"""
Wikipedia Search Tool for AgenticSeek
Searches Wikipedia and extracts content, images, and hyperlinks.
"""

import os
import sys
import re
import requests
from typing import Dict, List, Tuple, Optional

if __name__ == "__main__":
    sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from sources.tools.tools import Tools


class WikipediaSearch(Tools):
    def __init__(self, language: str = "en"):
        """
        Initialize Wikipedia Search tool.
        
        Args:
            language: Wikipedia language code (default: "en" for English)
        """
        super().__init__()
        self.tag = "wikipedia_search"
        self.name = "Wikipedia Search"
        self.description = "Search Wikipedia and extract article content, images, and hyperlinks"
        self.language = language
        self.api_base = f"https://{language}.wikipedia.org/w/api.php"
        self.max_images = 5
        self.max_links = 10

    def execute(self, blocks: List[str], safety: bool = True) -> str:
        """
        Execute Wikipedia search for the provided query.
        
        Args:
            blocks: List of query strings
            safety: Safety flag (not used for Wikipedia)
            
        Returns:
            Formatted article content with images and links
        """
        if not blocks or not blocks[0].strip():
            return "Error: No search query provided"
        
        # Parse query and options
        query, options = self._parse_query(blocks[0])
        
        if not query:
            return "Error: Empty search query"
        
        try:
            # Search for article
            page_title = self._search_article(query)
            if not page_title:
                suggestions = self._get_suggestions(query)
                if suggestions:
                    return f"Article not found. Did you mean:\n" + "\n".join(f"- {s}" for s in suggestions[:5])
                return f"No Wikipedia article found for: {query}"
            
            # Get article content
            content = self._get_article_content(page_title, options)
            
            # Get images if requested
            images = []
            if options.get("include_images", True):
                images = self._get_article_images(page_title, max_images=options.get("max_images", self.max_images))
            
            # Get links if requested
            links = []
            if options.get("include_links", True):
                links = self._get_article_links(page_title, max_links=options.get("max_links", self.max_links))
            
            # Format response
            response = self._format_response(page_title, content, images, links, options)
            
            return response
            
        except Exception as e:
            return f"Wikipedia search error: {str(e)}"

    def _parse_query(self, block: str) -> Tuple[str, Dict]:
        """
        Parse query string and extract options.
        
        Args:
            block: Raw query block
            
        Returns:
            Tuple of (query, options_dict)
        """
        options = {
            "include_images": True,
            "include_links": True,
            "summary_only": False,
            "max_images": self.max_images,
            "max_links": self.max_links
        }
        
        lines = block.strip().split('\n')
        query = ""
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
                
            # Check for parameter format
            if '=' in line:
                key, value = line.split('=', 1)
                key = key.strip().lower()
                value = value.strip()
                
                if key == "query":
                    query = value
                elif key == "images":
                    options["include_images"] = value.lower() in ["true", "yes", "1"]
                elif key == "links":
                    options["include_links"] = value.lower() in ["true", "yes", "1"]
                elif key == "summary":
                    options["summary_only"] = value.lower() in ["true", "yes", "1", "only"]
                elif key == "max_images":
                    try:
                        options["max_images"] = int(value)
                    except ValueError:
                        pass
                elif key == "max_links":
                    try:
                        options["max_links"] = int(value)
                    except ValueError:
                        pass
            else:
                # If no parameters, treat entire block as query
                if not query:
                    query = line
        
        return query, options

    def _search_article(self, query: str) -> Optional[str]:
        """
        Search Wikipedia for an article title.
        
        Args:
            query: Search query
            
        Returns:
            Article title or None if not found
        """
        params = {
            "action": "query",
            "format": "json",
            "list": "search",
            "srsearch": query,
            "srlimit": 1
        }
        
        response = requests.get(self.api_base, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        if data.get("query", {}).get("search"):
            return data["query"]["search"][0]["title"]
        
        return None

    def _get_suggestions(self, query: str) -> List[str]:
        """
        Get search suggestions for a query.
        
        Args:
            query: Search query
            
        Returns:
            List of suggested article titles
        """
        params = {
            "action": "opensearch",
            "format": "json",
            "search": query,
            "limit": 5
        }
        
        try:
            response = requests.get(self.api_base, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            return data[1] if len(data) > 1 else []
        except Exception:
            return []

    def _get_article_content(self, title: str, options: Dict) -> Dict:
        """
        Get article content from Wikipedia.
        
        Args:
            title: Article title
            options: Query options
            
        Returns:
            Dict with article data
        """
        params = {
            "action": "query",
            "format": "json",
            "titles": title,
            "prop": "extracts|info",
            "exintro": options.get("summary_only", False),
            "explaintext": True,
            "inprop": "url"
        }
        
        response = requests.get(self.api_base, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        page = next(iter(data["query"]["pages"].values()))
        
        return {
            "title": page.get("title", title),
            "extract": page.get("extract", ""),
            "url": page.get("fullurl", f"https://{self.language}.wikipedia.org/wiki/{title.replace(' ', '_')}")
        }

    def _get_article_images(self, title: str, max_images: int = 5) -> List[Dict]:
        """
        Get images from Wikipedia article.
        
        Args:
            title: Article title
            max_images: Maximum number of images to return
            
        Returns:
            List of image dicts with url and description
        """
        params = {
            "action": "query",
            "format": "json",
            "titles": title,
            "prop": "images",
            "imlimit": max_images * 2  # Get more to filter
        }
        
        response = requests.get(self.api_base, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        page = next(iter(data["query"]["pages"].values()))
        images_data = page.get("images", [])
        
        # Get image URLs
        images = []
        for img_data in images_data[:max_images * 2]:
            img_title = img_data.get("title", "")
            
            # Skip icons, logos (small files)
            if any(skip in img_title.lower() for skip in ["icon", "logo", ".svg"]):
                continue
            
            # Get image info
            img_url = self._get_image_url(img_title)
            if img_url:
                images.append({
                    "title": img_title.replace("File:", "").replace("_", " "),
                    "url": img_url
                })
            
            if len(images) >= max_images:
                break
        
        return images

    def _get_image_url(self, image_title: str) -> Optional[str]:
        """
        Get direct URL for an image.
        
        Args:
            image_title: Image title from Wikipedia
            
        Returns:
            Direct image URL or None
        """
        params = {
            "action": "query",
            "format": "json",
            "titles": image_title,
            "prop": "imageinfo",
            "iiprop": "url"
        }
        
        try:
            response = requests.get(self.api_base, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            page = next(iter(data["query"]["pages"].values()))
            if "imageinfo" in page and page["imageinfo"]:
                return page["imageinfo"][0].get("url")
        except Exception:
            pass
        
        return None

    def _get_article_links(self, title: str, max_links: int = 10) -> List[Dict]:
        """
        Get related article links.
        
        Args:
            title: Article title
            max_links: Maximum number of links to return
            
        Returns:
            List of link dicts with title and url
        """
        params = {
            "action": "query",
            "format": "json",
            "titles": title,
            "prop": "links",
            "pllimit": max_links,
            "plnamespace": 0  # Main namespace only
        }
        
        response = requests.get(self.api_base, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        page = next(iter(data["query"]["pages"].values()))
        links_data = page.get("links", [])
        
        links = []
        for link in links_data[:max_links]:
            link_title = link.get("title", "")
            links.append({
                "title": link_title,
                "url": f"https://{self.language}.wikipedia.org/wiki/{link_title.replace(' ', '_')}"
            })
        
        return links

    def _format_response(self, title: str, content: Dict, images: List[Dict], 
                        links: List[Dict], options: Dict) -> str:
        """
        Format the Wikipedia search response.
        
        Args:
            title: Article title
            content: Article content dict
            images: List of image dicts
            links: List of link dicts
            options: Query options
            
        Returns:
            Formatted markdown string
        """
        response_parts = []
        
        # Title
        response_parts.append(f"# {content['title']}")
        response_parts.append(f"\n**Source:** {content['url']}\n")
        
        # Content
        extract = content.get("extract", "")
        if extract:
            # Limit length if summary only
            if options.get("summary_only", False) and len(extract) > 1000:
                extract = extract[:1000] + "..."
            
            response_parts.append("## Summary" if options.get("summary_only", False) else "## Content")
            response_parts.append(f"\n{extract}\n")
        
        # Images
        if images and options.get("include_images", True):
            response_parts.append("## Images")
            for idx, img in enumerate(images, 1):
                response_parts.append(f"{idx}. ![{img['title']}]({img['url']})")
                response_parts.append(f"   *{img['title']}*")
            response_parts.append("")
        
        # Links
        if links and options.get("include_links", True):
            response_parts.append("## Related Articles")
            for link in links:
                response_parts.append(f"- [{link['title']}]({link['url']})")
            response_parts.append("")
        
        return "\n".join(response_parts)

    def execution_failure_check(self, output: str) -> bool:
        """
        Check if execution failed.
        
        Args:
            output: Tool output
            
        Returns:
            True if failed, False if successful
        """
        return output.startswith("Error:") or "not found" in output.lower()

    def interpreter_feedback(self, output: str) -> str:
        """
        Generate feedback for the LLM.
        
        Args:
            output: Tool output
            
        Returns:
            Feedback message
        """
        if self.execution_failure_check(output):
            return f"Wikipedia search failed: {output}"
        return f"Wikipedia article retrieved:\n{output}"


if __name__ == "__main__":
    # Test the Wikipedia search tool
    wiki = WikipediaSearch()
    
    # Test 1: Basic search
    print("=== Test 1: Basic Search ===")
    result = wiki.execute(["Quantum Computing"], safety=True)
    print(result[:500])  # Print first 500 chars
    print("\n" + "="*50 + "\n")
    
    # Test 2: Search with options
    print("=== Test 2: With Options ===")
    result = wiki.execute(["query=Python programming\nmax_images=2\nmax_links=5"], safety=True)
    print(result[:500])
    print("\n" + "="*50 + "\n")
    
    # Test 3: Summary only
    print("=== Test 3: Summary Only ===")
    result = wiki.execute(["query=Artificial Intelligence\nsummary=true"], safety=True)
    print(result[:500])

