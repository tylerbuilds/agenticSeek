#!/bin/bash
# Script to switch AgenticSeek to use Z.ai GLM provider

set -e

echo "=========================================="
echo "Switching AgenticSeek to Z.ai GLM"
echo "=========================================="
echo ""

# Check if config.ini exists
if [ ! -f "config.ini" ]; then
    echo "Error: config.ini not found!"
    exit 1
fi

# Backup current config
echo "1. Backing up current config..."
cp config.ini config_ollama_backup.ini
echo "   ✓ Backup saved to config_ollama_backup.ini"

# Update config.ini to use GLM
echo ""
echo "2. Updating config.ini for GLM..."
sed -i 's/is_local = True/is_local = False/' config.ini
sed -i 's/provider_name = ollama/provider_name = glm/' config.ini
sed -i 's/provider_model = deepseek-r1:14b/provider_model = glm-4-plus/' config.ini
sed -i 's|provider_server_address = http://host.docker.internal:11434|provider_server_address = |' config.ini
echo "   ✓ Config updated"

# Show changes
echo ""
echo "3. New configuration:"
echo "   -----------------------------------"
grep -E "(is_local|provider_name|provider_model)" config.ini
echo "   -----------------------------------"

# Stop current services
echo ""
echo "4. Stopping current services..."
docker compose --profile full down
echo "   ✓ Services stopped"

# Start with GLM
echo ""
echo "5. Starting AgenticSeek with GLM..."
./start_services.sh full &
sleep 5

echo ""
echo "=========================================="
echo "✓ Switch Complete!"
echo "=========================================="
echo ""
echo "AgenticSeek is now using Z.ai GLM-4-Plus"
echo ""
echo "Access at: http://localhost:3001"
echo ""
echo "To switch back to Ollama:"
echo "  cp config_ollama_backup.ini config.ini"
echo "  docker compose --profile full down"
echo "  ./start_services.sh full"
echo ""

