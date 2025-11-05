#!/usr/bin/env python3
"""
Test script for GLM 4.6 integration with AgenticSeek
This script tests the GLM provider implementation.
"""

import sys
import os

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from sources.llm_provider import Provider
from dotenv import load_dotenv

def test_glm_basic():
    """Test basic GLM functionality"""
    print("=" * 60)
    print("Testing GLM 4.6 Integration")
    print("=" * 60)
    
    # Load environment variables
    load_dotenv()
    
    # Create GLM provider
    print("\n1. Initializing GLM provider...")
    try:
        provider = Provider(
            provider_name="glm",
            model="glm-4-plus",  # GLM-4-Plus model
            is_local=False
        )
        print("   ✓ GLM provider initialized successfully")
    except Exception as e:
        print(f"   ✗ Failed to initialize: {e}")
        return False
    
    # Test simple query
    print("\n2. Testing simple query...")
    history = [
        {"role": "user", "content": "Say 'Hello from GLM!' in exactly those words."}
    ]
    
    try:
        response = provider.respond(history, verbose=True)
        print(f"\n   Response: {response}")
        print("   ✓ Query completed successfully")
    except Exception as e:
        print(f"   ✗ Query failed: {e}")
        return False
    
    # Test reasoning capability
    print("\n3. Testing reasoning capability...")
    history = [
        {"role": "user", "content": "What is 2+2? Explain your reasoning briefly."}
    ]
    
    try:
        response = provider.respond(history, verbose=False)
        print(f"\n   Response: {response}")
        print("   ✓ Reasoning test completed")
    except Exception as e:
        print(f"   ✗ Reasoning test failed: {e}")
        return False
    
    # Test Chinese language capability
    print("\n4. Testing Chinese language support...")
    history = [
        {"role": "user", "content": "请用中文回答：你好吗？"}
    ]
    
    try:
        response = provider.respond(history, verbose=False)
        print(f"\n   Response: {response}")
        print("   ✓ Chinese language test completed")
    except Exception as e:
        print(f"   ✗ Chinese language test failed: {e}")
        return False
    
    print("\n" + "=" * 60)
    print("All tests passed! ✓")
    print("=" * 60)
    return True


def test_glm_models():
    """Test different GLM models"""
    print("\n\nAvailable GLM Models:")
    print("-" * 60)
    models = [
        ("glm-4-plus", "Most capable model"),
        ("glm-4-0520", "Snapshot version"),
        ("glm-4", "Standard GLM-4"),
        ("glm-4-air", "Faster, lighter version"),
        ("glm-4-airx", "Extended context version"),
        ("glm-4-flash", "Fastest, most cost-effective"),
    ]
    
    for model, description in models:
        print(f"  • {model:20} - {description}")
    
    print("\nTo use a different model, update config.ini:")
    print("  provider_model = glm-4-plus")


if __name__ == "__main__":
    print("\nGLM 4.6 Integration Test")
    print("=" * 60)
    
    # Check if API key is set
    load_dotenv()
    api_key = os.getenv("GLM_API_KEY")
    
    if not api_key:
        print("ERROR: GLM_API_KEY not found in .env file")
        print("Please add your API key to .env:")
        print('  GLM_API_KEY="your-api-key-here"')
        sys.exit(1)
    
    print(f"API Key found: {api_key[:20]}...")
    
    # Run tests
    success = test_glm_basic()
    
    if success:
        test_glm_models()
        print("\n✓ GLM integration is working correctly!")
        print("\nNext steps:")
        print("  1. Update config.ini to use GLM:")
        print("     provider_name = glm")
        print("     provider_model = glm-4-plus")
        print("     is_local = False")
        print("  2. Restart AgenticSeek")
    else:
        print("\n✗ GLM integration test failed")
        print("Please check the error messages above")
        sys.exit(1)

