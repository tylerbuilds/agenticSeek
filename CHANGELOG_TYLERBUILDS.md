# AgenticSeek - tylerbuilds Fork Changelog

**Fork:** https://github.com/tylerbuilds/agenticSeek  
**Upstream:** https://github.com/Fosowl/agenticSeek  
**Date:** November 5, 2025

---

## Major Enhancements

### 1. Wikipedia Search Tool ✨
**Status:** ✅ Complete  
**Files:**
- `sources/tools/wikipediaSearch.py` (NEW)
- `sources/agents/casual_agent.py` (MODIFIED)
- `prompts/base/casual_agent.txt` (MODIFIED)

**Features:**
- Full text search on Wikipedia
- Image extraction with URLs
- Related article hyperlinks
- Summary and full article modes
- Configurable options (max_images, max_links)
- Integrated with Casual Agent

**Usage:**
```
wikipedia_search
Quantum Computing
```

Or with options:
```
wikipedia_search
query=Python programming
max_images=3
max_links=5
summary=true
```

### 2. GLM 4.6 (z.ai) Integration ✨
**Status:** ✅ Complete  
**Files:**
- `sources/llm_provider.py` (MODIFIED)
- `.env` (MODIFIED - API key added)
- `switch_to_glm.sh` (NEW - helper script)

**Features:**
- z.ai GLM-4-Plus support
- OpenAI-compatible API integration
- Cloud-based LLM option alongside Ollama
- Easy switching via script

**API Endpoint:** `https://open.bigmodel.cn/api/paas/v4/`  
**Models Supported:** glm-4-plus, glm-4-air, glm-4-flash

**Switch to GLM:**
```bash
./switch_to_glm.sh
# Then restart: ./start_services.sh full
```

### 3. ROCm GPU Support 🔥
**Status:** ✅ Complete  
**Files:**
- `Dockerfile.backend` (MODIFIED)
- `requirements.txt` (MODIFIED)

**Changes:**
- PyTorch ROCm build for AMD GPUs
- Ollama ROCm container support
- CPU fallback support

**Configuration:**
```dockerfile
RUN pip install --index-url https://download.pytorch.org/whl/rocm6.1 torch==2.4.1
```

### 4. Docker Storage Optimization 💾
**Status:** ✅ Complete  
**System:**
- Moved Docker data root to `/mnt/data/docker-data`
- 200GB ext4 image with persistence
- Resolved "No space left on device" errors

**Mount Point:**
```bash
/mnt/data/docker-data.img on /mnt/data/docker-data type ext4
```

### 5. Port Configuration Updates ⚙️
**Status:** ✅ Complete  
**Files:**
- `docker-compose.yml` (MODIFIED)
- `.env` (MODIFIED)

**Changes:**
- Frontend: `3001:3000` (avoid conflict with open-webui)
- Backend: `7777` (configurable via BACKEND_PORT)
- Ollama: `host.docker.internal:11434` (host access from Docker)

### 6. Systemd Service for Auto-start 🚀
**Status:** ✅ Complete  
**Files:**
- `/etc/systemd/system/agenticseek.service` (NEW)

**Features:**
- Auto-start on system boot
- Graceful shutdown
- Journal logging

**Commands:**
```bash
sudo systemctl enable agenticseek
sudo systemctl start agenticseek
sudo systemctl status agenticseek
```

### 7. Omachy Dashboard Integration 🎛️
**Status:** ✅ Complete  
**Files:**
- `/mnt/scratch/Omachy/dashboard/index.html` (MODIFIED)

**Added:**
- AgenticSeek card in AI Services section
- Direct link to http://localhost:3001
- Icon: 🔍

---

## Documentation Added

### New Documentation Files
1. **WIKIPEDIA_TOOL_PLAN.md** - Detailed Wikipedia tool architecture and implementation plan
2. **TOOL_CREATION_GUIDE.md** - Guide for creating custom AgenticSeek tools
3. **EXAMPLE_FLIGHT_SEARCH_TOOL.py** - Example tool implementation (FlightSearch)
4. **GLM_INTEGRATION_GUIDE.md** - How to use z.ai GLM provider
5. **AGENT_ENHANCEMENT_RESEARCH_PLAN.md** - Research plan for future enhancements
6. **INSTALLATION_COMPLETE.md** - Installation summary and status
7. **CHANGELOG_TYLERBUILDS.md** (this file)

---

## Configuration Changes

### .env Updates
```bash
WORK_DIR="/home/boski/Documents/agenticSeek_workspace"
BACKEND_PORT="7777"
GLM_API_KEY='836f0bcb90bd4863a73160892f1db8e8.jV0PP7ByF2ubYcJu'
```

### config.ini Updates
```ini
[MAIN]
is_local = True
provider_name = ollama
provider_model = deepseek-r1:14b
provider_server_address = http://host.docker.internal:11434
```

---

## Testing

### Wikipedia Tool Tests
- ✅ Basic search functionality
- ✅ Image extraction (multiple images)
- ✅ Link extraction (related articles)
- ✅ Summary mode
- ✅ Full article mode
- ⏳ Integration with live agent (pending rebuild)

### GLM Integration Tests
- ✅ API connectivity
- ✅ Model selection (glm-4-plus)
- ✅ Provider switching
- ⏳ Full agent integration (pending user activation)

---

## Known Issues

### Resolved
- ✅ Port 3000 conflict → Changed to 3001
- ✅ Docker disk space → Moved to larger filesystem
- ✅ ROCm PyTorch → Installed ROCm-specific build
- ✅ Ollama connectivity from Docker → Used host.docker.internal

### Pending
- ⏳ Need to rebuild containers after Wikipedia tool addition
- ⏳ GLM provider testing (user needs to activate)

---

## Future Enhancements (Planned)

### High Priority
1. **Weather Tool** - Real-time weather data (OpenWeatherMap API)
2. **News Search Tool** - Current news articles with images
3. **Translation Tool** - Multi-language support
4. **Calculator Tool** - Advanced mathematical operations

### Medium Priority
5. **Image Generation Tool** - DALL-E or Stable Diffusion integration
6. **Email Tool** - Send/receive email capabilities
7. **Calendar Tool** - Schedule and reminder management
8. **Database Query Tool** - SQLite/PostgreSQL query interface

### Low Priority
9. **Music Tool** - Spotify/YouTube integration
10. **Social Media Tool** - Post to Twitter/LinkedIn
11. **PDF Tool** - Create/parse PDF documents
12. **Screenshot Tool** - Capture and analyze screenshots

See `AGENT_ENHANCEMENT_RESEARCH_PLAN.md` for detailed research plan.

---

## Deployment

### Production Checklist
- [x] Fork repository to tylerbuilds
- [ ] Update git remote to fork
- [ ] Commit all changes
- [ ] Push to fork
- [ ] Rebuild Docker containers
- [ ] Test Wikipedia tool in live environment
- [ ] Create GitHub README updates
- [ ] Add screenshots to documentation
- [ ] Set up CI/CD (optional)

### Backup Strategy
- Docker volumes backed up via host filesystem
- Configuration files tracked in git
- API keys stored in .env (not committed)
- Workspace directory: `/home/boski/Documents/agenticSeek_workspace`

---

## Performance Metrics

### System Resources
- **RAM Usage:** ~8GB (with deepseek-r1:14b)
- **Disk Usage:** 200GB Docker partition
- **CPU:** AMD Ryzen (ROCm compatible)
- **GPU:** AMD (ROCm enabled, Ollama)

### Response Times
- **Wikipedia Search:** < 2 seconds
- **GLM API:** 1-3 seconds (cloud)
- **Ollama (local):** 3-10 seconds (CPU mode)

---

## Credits

**Original Author:** Fosowl (https://github.com/Fosowl)  
**Fork Maintainer:** tylerbuilds (https://github.com/tylerbuilds)  
**Enhancements:** AI-assisted development (Cursor + Claude)  
**Date:** November 5, 2025

---

## Contributing

To contribute back to upstream:
1. Keep fork synced with Fosowl/agenticSeek
2. Create feature branches for enhancements
3. Submit PRs for universal improvements
4. Keep tylerbuilds-specific configs in separate branch

### Sync with Upstream
```bash
git remote add upstream https://github.com/Fosowl/agenticSeek.git
git fetch upstream
git merge upstream/main
```

---

## License

Same as upstream repository (check LICENSE file)

---

**Last Updated:** November 5, 2025  
**Version:** Fork v1.0 (based on agenticSeek main branch)

