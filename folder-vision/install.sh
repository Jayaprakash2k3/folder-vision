#!/bin/bash
# Unix installer script for folder-vision
set -e

echo "🚀 Installing folder-vision..."

# Install the package
if command -v pipx >/dev/null 2>&1; then
    echo "📦 Using pipx (recommended)"
    pipx install folder-vision
    echo "✅ Installation complete!"
    echo "🌐 Starting server..."
    folder-vision
else
    echo "📦 Using pip"
    python3 -m pip install --user folder-vision
    
    # Test if command works
    if command -v folder-vision >/dev/null 2>&1; then
        echo "✅ Installation complete!"
        echo "🌐 Starting server..."
        folder-vision
    else
        echo "⚠️  Command not found, setting up PATH..."
        python3 setup_path.py
        echo "✅ Setup complete!"
        echo "🌐 Starting server via module..."
        python3 -m folder_vision
    fi
fi