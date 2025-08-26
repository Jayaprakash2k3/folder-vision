#!/bin/bash

# Quick test script for uv installation
echo "🧪 Testing folder-vision installation with uv..."

# Check if uv is installed
if ! command -v uv &> /dev/null; then
    echo "❌ uv not found. Installing uv..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    source ~/.bashrc 2>/dev/null || source ~/.zshrc 2>/dev/null || true
fi

echo "✅ uv found: $(uv --version)"

# Install folder-vision
echo "📦 Installing folder-vision..."
uv tool install folder-vision --force

# Test the command
echo "🔧 Testing folder-vision command..."
if command -v folder-vision &> /dev/null; then
    echo "✅ folder-vision command found"
    folder-vision --version
    folder-vision --help | head -5
    echo "✅ All tests passed! folder-vision is ready to use."
else
    echo "❌ folder-vision command not found. Checking uv tool list..."
    uv tool list
fi

echo ""
echo "🚀 Quick start:"
echo "  cd ~/Pictures"
echo "  folder-vision serve"
echo "  # Open http://localhost:8000 in your browser"