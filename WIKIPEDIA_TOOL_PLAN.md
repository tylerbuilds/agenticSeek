# Wikipedia Search Tool - Implementation Plan

**Created:** 2025-11-05  
**Status:** Planning → Implementation  
**Priority:** High (Quick Win)

---

## Overview

Build a comprehensive Wikipedia search tool that provides:
- Text content from Wikipedia articles
- Images from articles (with URLs)
- Hyperlinks to related articles
- Summary and full article options

---

## Tool Specifications

### Tool Name
`wikipedia_search` or `wiki`

### Capabilities

1. **Search Wikipedia**
   - Query Wikipedia API
   - Return most relevant article
   - Support for multiple languages (start with English)

2. **Extract Content**
   - Article title
   - Summary (first paragraph)
   - Full content (optional)
   - Section headings

3. **Extract Images**
   - Main article image (if available)
   - Additional images from article (up to N images)
   - Image URLs (direct links)
   - Image captions/descriptions

4. **Extract Links**
   - Related articles (hyperlinks)
   - External references
   - Categories
   - See also section

### Input Format

```wikipedia_search
query=Quantum Computing
sections=summary,images,links
max_images=3
```

Or simple:
```wikipedia_search
Quantum Computing
```

### Output Format

```markdown
# Article Title

## Summary
[First paragraph or summary]

## Main Content
[Article text - optional, can be summary only]

## Images
- ![Image 1](URL) - Caption
- ![Image 2](URL) - Caption

## Related Links
- [Related Article 1](URL)
- [Related Article 2](URL)

## References
[External links]
```

---

## Technical Implementation

### API Choice

**Option 1: Wikipedia API (Official)**
- Endpoint: `https://en.wikipedia.org/w/api.php`
- Free, no API key needed
- Well documented
- Rate limits: reasonable for our use

**Option 2: Wikipedia Python Library**
- Package: `wikipedia-api` or `wikipedia`
- Easier to use
- Built-in parsing
- Less flexible

**Decision: Use both**
- Wikipedia library for main content
- Direct API calls for images/advanced features

### Dependencies

Add to `requirements.txt`:
```
wikipedia-api>=0.6.0
beautifulsoup4>=4.12.0
requests>=2.31.0
```

---

## Implementation Steps

### Phase 1: Basic Search (30 min)

1. Create `wikipediaSearch.py` in `sources/tools/`
2. Implement basic search functionality
3. Return article summary
4. Test with simple queries

### Phase 2: Image Extraction (30 min)

1. Add image extraction from Wikipedia API
2. Get main article image
3. Get additional content images
4. Format image URLs properly

### Phase 3: Link Extraction (20 min)

1. Extract related articles
2. Extract categories
3. Extract references
4. Format as clickable links

### Phase 4: Integration (20 min)

1. Add tool to casual_agent
2. Update agent prompt
3. Test full workflow

---

## Code Structure

```python
class WikipediaSearch(Tools):
    def __init__(self):
        super().__init__()
        self.tag = "wikipedia_search"
        self.name = "Wikipedia Search"
        self.description = "Search Wikipedia and extract content, images, and links"
        
    def execute(self, blocks, safety=True):
        # Parse query
        # Search Wikipedia
        # Extract content
        # Extract images
        # Extract links
        # Format response
        
    def _search_article(self, query):
        # Search and get article
        
    def _extract_images(self, page):
        # Get images from article
        
    def _extract_links(self, page):
        # Get related links
        
    def _format_response(self, content, images, links):
        # Format markdown output
```

---

## Usage Examples

### Example 1: Quick Summary
```
User: "Tell me about quantum computing"
Agent: Uses wikipedia_search
Result: Summary + main image + related links
```

### Example 2: Detailed Research
```
User: "Research artificial intelligence and save to ai_research.txt"
Agent: Uses wikipedia_search (full content) + file tools
Result: Comprehensive article saved with images and links
```

### Example 3: Multi-topic
```
User: "Compare Python and JavaScript"
Agent: Uses wikipedia_search twice, combines results
Result: Side-by-side comparison with images
```

---

## Advanced Features (Future)

### Phase 5: Enhanced Capabilities (Future)

1. **Multi-language Support**
   - Detect query language
   - Search in appropriate Wikipedia
   - Return results in original language

2. **Image Download**
   - Optionally download images to workspace
   - Reference local files instead of URLs
   - Useful for offline access

3. **Section-Specific Search**
   - Target specific sections (History, Applications, etc.)
   - More focused results

4. **Comparison Mode**
   - Compare multiple topics
   - Side-by-side format

5. **Citation Export**
   - Generate proper citations
   - BibTeX format
   - APA/MLA format

---

## Testing Plan

### Unit Tests

1. **Search Functionality**
   - Valid query returns results
   - Invalid query returns error
   - Ambiguous query suggests alternatives

2. **Image Extraction**
   - Articles with images return URLs
   - Articles without images handle gracefully
   - Image URLs are valid

3. **Link Extraction**
   - Related links are relevant
   - Links are properly formatted
   - External references included

### Integration Tests

1. **With Casual Agent**
   - Natural language query → Wikipedia search
   - Results formatted properly
   - Agent can use results in response

2. **With File Agent**
   - Search + save to file
   - Images included in saved content

3. **With Web Agent**
   - Wikipedia as starting point
   - Links used for further research

---

## Error Handling

### Common Errors

1. **Article Not Found**
   - Suggest similar articles
   - Return "No results found"

2. **Disambiguation Page**
   - List options
   - Ask user to clarify

3. **Network Error**
   - Retry mechanism
   - Fallback to cached data (future)

4. **API Rate Limit**
   - Implement backoff
   - Queue requests

---

## Performance Considerations

### Optimization

1. **Caching**
   - Cache article content (1 hour TTL)
   - Cache images (longer TTL)
   - Reduce API calls

2. **Lazy Loading**
   - Load summary first
   - Load images only if requested
   - Load full content only if needed

3. **Parallel Requests**
   - Fetch content and images in parallel
   - Faster response time

---

## Integration Points

### Agents That Can Use Wikipedia Tool

1. **Casual Agent** ✓ (Primary)
   - General knowledge questions
   - Quick facts

2. **Research Agent** (Future)
   - Academic research
   - Comprehensive articles

3. **Web Agent**
   - Starting point for research
   - Verify information

4. **Code Agent**
   - Programming concept documentation
   - Algorithm explanations

---

## Success Metrics

### Functionality
- ✓ Returns relevant articles for 95% of queries
- ✓ Extracts at least 1 image for 80% of articles
- ✓ Provides 5+ related links per article

### Performance
- < 2 seconds for summary
- < 5 seconds for full article with images
- < 1 second for cached results

### User Experience
- Clear, formatted output
- Images displayed inline (if agent supports)
- Clickable links in web UI

---

## Documentation Requirements

1. **User Guide**
   - How to use Wikipedia tool
   - Query formats
   - Example queries

2. **Developer Guide**
   - API reference
   - Extension points
   - Custom formatters

3. **Prompt Updates**
   - Add to agent prompts
   - Usage examples
   - When to use Wikipedia vs web_search

---

## Rollout Plan

### Phase 1: Development (Today)
- [ ] Implement basic tool
- [ ] Add image extraction
- [ ] Add link extraction
- [ ] Unit tests

### Phase 2: Integration (Today)
- [ ] Add to casual_agent
- [ ] Update prompts
- [ ] Integration tests

### Phase 3: Testing (Today)
- [ ] Manual testing
- [ ] Edge cases
- [ ] Performance testing

### Phase 4: Documentation (Today)
- [ ] User documentation
- [ ] Code documentation
- [ ] Update README

---

## Next Steps

1. **Immediate:**
   - Install `wikipedia-api` package
   - Create `wikipediaSearch.py`
   - Implement basic search

2. **Short-term:**
   - Add image extraction
   - Add link extraction
   - Integrate with agent

3. **Long-term:**
   - Multi-language support
   - Caching layer
   - Advanced features

---

**Estimated Time:** 2 hours total
- Planning: 15 min ✓
- Basic implementation: 30 min
- Image/link extraction: 50 min
- Integration: 20 min
- Testing: 15 min
- Documentation: 10 min

---

**Status:** Ready to implement! 🚀

