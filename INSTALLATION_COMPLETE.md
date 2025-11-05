# AgenticSeek Installation Complete

## ✅ What Was Done

1. **Repository Cloned**: AgenticSeek has been cloned to `/mnt/data/projects/agfentSeek`

2. **Port Configuration**: 
   - Frontend port changed from 3000 to **3001** (to avoid conflict with open-webui)
   - Backend port: **7777**
   - SearXNG port: **8080**
   - Redis port: **6379** (internal)

3. **Configuration Files**:
   - `.env` file created with your workspace directory
   - `config.ini` updated to use `http://host.docker.internal:11434` for Ollama access
   - Workspace directory created: `/home/boski/Documents/agenticSeek_workspace`

4. **Auto-Start on Reboot**:
   - Systemd service created: `agenticseek.service`
   - Service enabled for automatic startup on reboot

## 🚀 How to Start AgenticSeek

### Option 1: Manual Start (Recommended for First Time)
```bash
cd /mnt/data/projects/agfentSeek
./start_services.sh full
```

### Option 2: Using Systemd Service
```bash
sudo systemctl start agenticseek
```

### Option 3: Check Service Status
```bash
sudo systemctl status agenticseek
```

## 📍 Access Points

- **Web Interface**: http://localhost:3001
- **Backend API**: http://localhost:7777
- **SearXNG**: http://localhost:8080
- **Ollama** (already running): http://localhost:11434

## ⚠️ Important: Download the Model First!

Before using AgenticSeek, you need to download the AI model in Ollama:

```bash
ollama pull deepseek-r1:14b
```

Or if you prefer a different model size:
- `deepseek-r1:7b` (smaller, faster)
- `deepseek-r1:32b` (larger, more capable)
- `deepseek-r1:70b` (largest, most capable)

**Note**: The model size you choose depends on your GPU VRAM:
- 7B: 8GB VRAM (not recommended, poor performance)
- 14B: 12GB VRAM (minimum recommended)
- 32B: 24GB+ VRAM (recommended)
- 70B: 48GB+ VRAM (best performance)

## 🔧 Service Management

### Start Services
```bash
sudo systemctl start agenticseek
```

### Stop Services
```bash
sudo systemctl stop agenticseek
```

### Restart Services
```bash
sudo systemctl restart agenticseek
```

### View Logs
```bash
# Systemd logs
sudo journalctl -u agenticseek -f

# Docker container logs
docker logs backend
docker logs frontend
docker logs searxng
```

### Check Service Status
```bash
sudo systemctl status agenticseek
docker ps  # Should show: backend, frontend, searxng, redis containers
```

## 📁 Workspace Directory

Your workspace is configured at: `/home/boski/Documents/agenticSeek_workspace`

AgenticSeek will read and write files in this directory. You can:
- Place files here for AgenticSeek to analyze
- AgenticSeek will save generated files here

## 🔄 Auto-Start on Reboot

The service is already enabled and will start automatically on reboot.

To disable auto-start:
```bash
sudo systemctl disable agenticseek
```

To re-enable:
```bash
sudo systemctl enable agenticseek
```

## 🐛 Troubleshooting

### Port Conflicts
If you get port conflicts:
- Check what's using the port: `netstat -tuln | grep <port>`
- Modify ports in `docker-compose.yml` if needed

### Ollama Connection Issues
If AgenticSeek can't connect to Ollama:
1. Verify Ollama is running: `docker ps | grep ollama`
2. Test Ollama: `curl http://localhost:11434/api/tags`
3. Check model is downloaded: `ollama list`

### Container Issues
If containers fail to start:
```bash
# View logs
docker logs backend
docker logs frontend

# Rebuild containers
cd /mnt/data/projects/agfentSeek
docker compose --profile full build
```

### Service Won't Start
```bash
# Check service status
sudo systemctl status agenticseek

# View detailed logs
sudo journalctl -u agenticseek -n 50
```

## 📝 Configuration Files

- **`.env`**: Environment variables (ports, API keys, workspace)
- **`config.ini`**: AgenticSeek configuration (model, provider, behavior)
- **`docker-compose.yml`**: Docker service definitions

## 🎯 Next Steps

1. **Download the model**: `ollama pull deepseek-r1:14b`
2. **Start the services**: `./start_services.sh full` or `sudo systemctl start agenticseek`
3. **Wait for backend**: Services may take 5-10 minutes to fully start on first run
4. **Access web interface**: Open http://localhost:3001 in your browser
5. **Start using AgenticSeek**: Try asking it to search the web or write code!

## 📚 Additional Resources

- Official Documentation: https://github.com/Fosowl/agenticSeek
- Troubleshooting: See README.md Troubleshooting section
- Discord Community: https://discord.gg/8hGDaME3TC

