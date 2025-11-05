# AgenticSeek - tylerbuilds Enhanced Fork 🚀

[![Original](https://img.shields.io/badge/Original-Fosowl%2FagenticSeek-blue)](https://github.com/Fosowl/agenticSeek)
[![Fork](https://img.shields.io/badge/Fork-tylerbuilds-green)](https://github.com/tylerbuilds/agenticSeek)
[![License](https://img.shields.io/badge/License-Same_as_Original-yellow)]()

**Enhanced autonomous AI agent with Wikipedia search, GLM 4.6 integration, and ROCm support**

---

## 🆕 What's New in This Fork

### 1. 📚 Wikipedia Search Tool
Full Wikipedia integration with image and hyperlink extraction:
- Search any Wikipedia article
- Extract images with URLs
- Get related article links
- Summary or full article modes

### 2. 🤖 GLM 4.6 (z.ai) Integration
Cloud LLM provider alongside Ollama:
- z.ai GLM-4-Plus support
- OpenAI-compatible API
- Easy switching with included script

### 3. 🔥 ROCm GPU Support
Optimized for AMD GPUs:
- PyTorch ROCm build
- Ollama ROCm container
- CPU fallback support

### 4. ⚙️ Production-Ready Setup
- Systemd service for auto-start
- Docker storage optimization
- Port conflict resolution
- Omachy Dashboard integration

---

## 🚀 Quick Start

### Prerequisites
- Docker & Docker Compose
- Ollama (for local LLM)
- 46GB+ RAM for local models
- AMD GPU (optional, for ROCm)

### Installation

1. **Clone this fork:**
```bash
git clone https://github.com/tylerbuilds/agenticSeek.git
cd agenticSeek
```

2. **Configure environment:**
```bash
cp .env.example .env
# Edit .env with your settings
```

3. **Start services:**
```bash
./start_services.sh full
```

4. **Access the interface:**
- Frontend: http://localhost:3001
- Backend API: http://localhost:7777
- Ollama: http://localhost:11434

---

## 📖 New Documentation

- **[WIKIPEDIA_TOOL_PLAN.md](WIKIPEDIA_TOOL_PLAN.md)** - Wikipedia tool architecture
- **[GLM_INTEGRATION_GUIDE.md](GLM_INTEGRATION_GUIDE.md)** - How to use z.ai GLM
- **[TOOL_CREATION_GUIDE.md](TOOL_CREATION_GUIDE.md)** - Create custom tools
- **[CHANGELOG_TYLERBUILDS.md](CHANGELOG_TYLERBUILDS.md)** - Complete changelog
- **[AGENT_ENHANCEMENT_RESEARCH_PLAN.md](AGENT_ENHANCEMENT_RESEARCH_PLAN.md)** - Future plans

---

## 🎯 Usage Examples

### Wikipedia Search
Ask the agent knowledge questions:
```
You: "What is quantum computing?"
Agent: *Uses wikipedia_search*
Result: Article with images and related links
```

### GLM Cloud LLM
Switch to cloud-based GLM:
```bash
./switch_to_glm.sh
./start_services.sh full
```

### ROCm GPU Acceleration
The backend automatically uses ROCm if AMD GPU is detected:
```bash
# Check GPU usage
docker logs backend | grep -i rocm
```

---

## 🛠️ Configuration

### Local LLM (Ollama)
```ini
# config.ini
[MAIN]
is_local = True
provider_name = ollama
provider_model = deepseek-r1:14b
provider_server_address = http://host.docker.internal:11434
```

### Cloud LLM (GLM)
```ini
# config.ini
[MAIN]
is_local = False
provider_name = glm
provider_model = glm-4-plus
```

### Environment Variables
```bash
# .env
WORK_DIR="/home/boski/Documents/agenticSeek_workspace"
BACKEND_PORT="7777"
GLM_API_KEY="your_api_key_here"
```

---

## 🔧 Systemd Service (Auto-start)

Enable auto-start on boot:
```bash
sudo systemctl enable agenticseek
sudo systemctl start agenticseek
sudo systemctl status agenticseek
```

---

## 🐛 Troubleshooting

### Port Conflicts
If port 3001 is in use:
```yaml
# docker-compose.yml
frontend:
  ports:
    - "YOUR_PORT:3000"  # Change YOUR_PORT
```

### Docker Space Issues
This fork includes automatic Docker storage management:
- Data root: `/mnt/data/docker-data`
- 200GB partition

### Ollama Connection
Containers use `host.docker.internal:11434` to access host Ollama:
```ini
provider_server_address = http://host.docker.internal:11434
```

---

## 📊 Performance

| Component | Resource Usage |
|-----------|----------------|
| RAM | ~8GB (deepseek-r1:14b) |
| Disk | 200GB Docker partition |
| CPU | AMD Ryzen |
| GPU | AMD (ROCm enabled) |

| Operation | Response Time |
|-----------|---------------|
| Wikipedia Search | < 2 seconds |
| GLM API | 1-3 seconds |
| Ollama (CPU) | 3-10 seconds |

---

## 🤝 Contributing

### To This Fork
1. Create feature branch
2. Make changes
3. Submit PR to tylerbuilds/agenticSeek

### To Upstream
1. Sync with Fosowl/agenticSeek
2. Cherry-pick universal improvements
3. Submit PR to original repo

---

## 🗺️ Roadmap

### Completed ✅
- [x] Wikipedia search tool
- [x] GLM 4.6 integration
- [x] ROCm GPU support
- [x] Systemd service
- [x] Port configuration
- [x] Docker optimization

### In Progress 🔄
- [ ] Weather tool (OpenWeatherMap)
- [ ] News search tool
- [ ] Translation tool
- [ ] Calculator tool

### Planned 📋
- [ ] Image generation (DALL-E/SD)
- [ ] Email integration
- [ ] Calendar management
- [ ] Database query tool

See [AGENT_ENHANCEMENT_RESEARCH_PLAN.md](AGENT_ENHANCEMENT_RESEARCH_PLAN.md) for details.

---

## 📜 License

Same as original repository. Check LICENSE file.

---

## 🙏 Credits

**Original Author:** [Fosowl](https://github.com/Fosowl)  
**Fork Maintainer:** [tylerbuilds](https://github.com/tylerbuilds)  
**Enhanced with:** Cursor + Claude AI  

---

## 📞 Support

- **Issues:** https://github.com/tylerbuilds/agenticSeek/issues
- **Original Repo:** https://github.com/Fosowl/agenticSeek
- **Documentation:** See docs in this repo

---

**Last Updated:** November 5, 2025  
**Version:** Fork v1.0

**⭐ If you find this fork useful, please star the repo!**

