# Z.ai GLM Integration Guide

**Date:** 2025-11-05  
**Status:** ✅ Integrated and Ready  
**Provider:** Z.ai (formerly Zhipu AI)

---

## Summary

GLM (General Language Model) from z.ai has been successfully integrated into AgenticSeek. This adds a powerful cloud-based LLM option alongside your local Ollama setup.

### What is Z.ai GLM-4.6?

- **Advanced reasoning** capabilities
- **200K token context** window
- **Superior coding** performance (48.6% win rate vs Claude Sonnet 4)
- **Multi-language** support (excellent Chinese language understanding)
- **Tool use** during inference
- **Cost-effective** compared to GPT-4

---

## Configuration

### API Key (Already Added)

Your z.ai API key has been added to `.env`:
```bash
GLM_API_KEY='836f0bcb90bd4863a73160892f1db8e8.jV0PP7ByF2ubYcJu'
```

### Available Models

| Model | Description | Use Case |
|-------|-------------|----------|
| `glm-4-plus` | Most capable, newest features | Complex reasoning, coding |
| `glm-4-0520` | Stable snapshot version | Production use |
| `glm-4` | Standard GLM-4 | General purpose |
| `glm-4-air` | Faster, lighter | Quick responses |
| `glm-4-airx` | Extended context | Long documents |
| `glm-4-flash` | Fastest, cheapest | Simple tasks |

**Recommendation:** Start with `glm-4-plus` for best results with GLM-4.6 features.

---

## How to Use GLM

### Option 1: Switch to GLM as Primary Provider

Edit `config.ini`:

```ini
[MAIN]
is_local = False
provider_name = glm
provider_model = glm-4-plus
provider_server_address = 
agent_name = Jarvis
```

Then restart AgenticSeek:
```bash
cd /mnt/data/projects/agfentSeek
docker compose --profile full down
./start_services.sh full
```

### Option 2: Keep Ollama Primary, Use GLM for Specific Tasks

Keep your current config with Ollama, but create a separate config file for GLM:

```bash
cp config.ini config_glm.ini
```

Edit `config_glm.ini`:
```ini
[MAIN]
is_local = False
provider_name = glm
provider_model = glm-4-plus
```

Then you can switch between them as needed.

### Option 3: Multi-LLM Router (Future Enhancement)

We can implement intelligent routing that automatically:
- Uses Ollama (local) for privacy-sensitive tasks
- Uses GLM (cloud) for complex reasoning or Chinese language
- Falls back between them based on availability

---

## When to Use GLM vs Ollama

### Use GLM (Z.ai) For:
✅ Complex reasoning tasks  
✅ Chinese language queries  
✅ Advanced coding tasks  
✅ Large context (up to 200K tokens)  
✅ When you need the absolute best performance  
✅ Tasks requiring tool use  

### Use Ollama (Local) For:
✅ Privacy-sensitive data  
✅ No internet connection  
✅ Cost-free operation  
✅ Simple queries  
✅ When speed matters more than quality  

---

## Testing GLM Integration

### Quick Test via Backend API

Once AgenticSeek is running with GLM configured:

```bash
curl -X POST http://localhost:7777/chat \
  -H "Content-Type: application/json" \
  -d '{
    "message": "Hello from GLM! What model are you?",
    "agent_type": "casual"
  }'
```

### Test in the Web UI

1. Open http://localhost:3001
2. Type a query: "Tell me about yourself"
3. GLM should respond with its capabilities

---

## Cost Considerations

Z.ai GLM API pricing (approximate):
- **GLM-4-Plus:** ~$0.015 per 1K tokens (input), ~$0.03 per 1K tokens (output)
- **GLM-4-Flash:** ~$0.0001 per 1K tokens (much cheaper)

**Tip:** Start with GLM-4-Plus to evaluate, then switch to GLM-4-Flash for production if cost is a concern.

---

## Troubleshooting

### Error: "GLM response is empty"
- Check API key in `.env`
- Verify network connection
- Check z.ai service status at https://z.ai

### Error: "GLM API is not available for local use"
- Set `is_local = False` in `config.ini`

### Error: "API key not found"
- Ensure `GLM_API_KEY` is in `.env` file
- Restart Docker containers after adding key

### API Rate Limits
If you hit rate limits:
- Add delays between requests
- Consider upgrading your z.ai plan
- Fall back to Ollama for some queries

---

## Example Queries for GLM

### Reasoning Task
```
"Explain the Monty Hall problem step by step with clear reasoning"
```

### Coding Task
```
"Write a Python function to solve the traveling salesman problem using dynamic programming"
```

### Chinese Language
```
"用中文解释量子计算的基本原理"
```

### Long Context
```
"Analyze this entire document and provide key insights: [paste large text]"
```

---

## Next Steps

1. **Try GLM Now:**
   ```bash
   cd /mnt/data/projects/agfentSeek
   # Backup current config
   cp config.ini config_ollama_backup.ini
   
   # Switch to GLM
   sed -i 's/is_local = True/is_local = False/' config.ini
   sed -i 's/provider_name = ollama/provider_name = glm/' config.ini
   sed -i 's/provider_model = deepseek-r1:14b/provider_model = glm-4-plus/' config.ini
   
   # Restart
   docker compose --profile full down
   ./start_services.sh full
   ```

2. **Monitor Usage:**
   - Track your API usage at https://z.ai (dashboard)
   - Monitor costs to avoid surprises
   - Adjust model choice based on needs

3. **Optimize:**
   - Use GLM-4-Flash for simple tasks
   - Use GLM-4-Plus for complex reasoning
   - Keep Ollama for privacy-sensitive work

---

## Advanced: Hybrid Setup

For the best of both worlds, you can create a **dual-provider setup**:

```bash
# Terminal 1: Run with Ollama (local)
config_file=config_ollama.ini ./start_services.sh full

# Terminal 2: Run with GLM (cloud) on different port
# Edit docker-compose.yml to use different ports
# Then start with GLM config
```

Or implement the **Multi-LLM Router** from the enhancement plan to automatically choose the best model for each task.

---

## References

- **Z.ai Platform:** https://z.ai
- **Chat Interface:** https://chat.z.ai
- **API Docs:** https://docs.z.ai
- **Model Info:** https://z.ai/blog/glm-4.6
- **AgenticSeek Docs:** /mnt/data/projects/agfentSeek/README.md

---

## Support

For issues with:
- **Z.ai API:** Contact z.ai support
- **AgenticSeek Integration:** Check logs in `provider.log`
- **This Integration:** Review `/mnt/data/projects/agfentSeek/sources/llm_provider.py`

---

**Status:** Ready to use! 🚀  
**Integrated by:** AI Assistant  
**Date:** 2025-11-05

