# Folder Vision - CLIP Image Search 🔍

> The fastest way to search your images with AI - powered by OpenAI's CLIP model

**✨ Just point it at any folder and search your images using natural language!**

```bash
# Install with uv (one command, works everywhere)
uv tool install folder-vision

# Go to any folder with images and start searching
cd ~/Pictures
folder-vision serve
```

Open `http://localhost:8000` in your browser and search with phrases like:

- "sunset over mountains"
- "cat sleeping on couch"
- "red sports car"
- "food on a plate"

## 🚀 Quick Start (2 minutes)

### 1. Install uv (if you don't have it)

**macOS/Linux:**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows:**

```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. Install Folder Vision

```bash
uv tool install folder-vision
```

### 3. Start Searching Your Images

```bash
# Navigate to any folder with images
cd ~/Pictures        # or ~/Desktop or any folder
cd /path/to/photos    # or wherever your images are

# Start the search engine
folder-vision serve
```

### 4. Open Your Browser

Go to `http://localhost:8000` and start searching!

## ✨ Why Use uv?

**uv** is the fastest Python package manager and handles everything automatically:

- ✅ **No PATH issues**: Commands work immediately after install
- ✅ **Isolated environment**: Doesn't conflict with other Python packages  
- ✅ **Cross-platform**: Same commands work on Windows, macOS, and Linux
- ✅ **Faster**: Installs packages 10-100x faster than pip
- ✅ **No virtual environment needed**: Handles isolation automatically

## 🔍 What You Can Do

### Search Your Images with Natural Language

```text
"dog playing in park"
"red car in driveway" 
"food on table"
"sunset landscape"
"person wearing glasses"
"flowers in garden"
```

### Find Similar Images

Upload any image to find visually similar ones in your collection.

### Browse and Cluster

- **Gallery View**: See all your images with thumbnails
- **Auto-Clustering**: Automatically group similar images together
- **Statistics**: See how many images are indexed

## 🖥️ Command Line Usage

### Basic Commands

```bash
# Start web interface (auto-indexes current directory)
folder-vision serve

# Start on different port
folder-vision serve --port 3000

# Index a specific folder
folder-vision index /path/to/images

# Search from command line
folder-vision search-text "red sports car"

# Find similar images to a file
folder-vision search-image /path/to/photo.jpg

# See statistics
folder-vision stats

# Get help
folder-vision --help
```

### Auto-Indexing Magic

Folder Vision automatically indexes whatever directory you're in:

```bash
cd ~/Pictures/Vacation2024
folder-vision serve    # Indexes all vacation photos

cd ~/Documents/Screenshots  
folder-vision serve    # Indexes all screenshots

cd /work/product-photos
folder-vision serve    # Indexes all product photos
```

No need to specify paths - it just works!

## 🎯 Real-World Examples

### Personal Photo Management

```bash
cd ~/Pictures
folder-vision serve
# Search: "family gathering", "birthday party", "beach vacation"
```

### Work Projects

```bash
cd ~/work/product-images
folder-vision serve  
# Search: "red shoes", "outdoor furniture", "kitchen appliances"
```

### Design Assets

```bash
cd ~/design/assets
folder-vision serve
# Search: "minimalist logo", "blue backgrounds", "vintage textures"
```

### Screenshot Organization

```bash
cd ~/Desktop/Screenshots
folder-vision serve
# Search: "error message", "code editor", "web page"
```

## ⚙️ System Requirements

- **Python**: 3.9+ (automatically handled by uv)
- **Memory**: 4GB+ recommended
- **Images**: Supports JPG, PNG, GIF, BMP, TIFF
- **Internet**: Only needed for initial model download

## 🛠️ Advanced Usage

### Custom Configuration

```bash
# Bind to all interfaces
folder-vision serve --host 0.0.0.0 --port 8000

# Development mode with auto-reload
folder-vision serve --reload

# Specify custom folder to index
folder-vision serve --index-dir /path/to/images
```

### Clustering and Analysis

```bash
# Automatically cluster similar images
folder-vision cluster

# Preview clusters without full analysis
folder-vision cluster-preview

# Export clustering results
folder-vision cluster --export clusters.json
```

## 🔧 Troubleshooting

### If uv is not found after installation

**Restart your terminal** or run:

```bash
# macOS/Linux
source ~/.bashrc
# or
source ~/.zshrc

# Windows
# Restart PowerShell or Command Prompt
```

### If folder-vision command is not found

```bash
# Check if it's installed
uv tool list

# Reinstall if needed
uv tool install folder-vision --force
```

### For large image collections

```bash
# Index in chunks for better performance
folder-vision index /huge/folder --batch-size 100

# Use GPU if available (much faster)
folder-vision serve --device cuda
```

## 🚀 Alternative Installation Methods

If you can't use uv for some reason:

### Using pipx (Second best option)

```bash
pipx install folder-vision
folder-vision serve
```

### Using pip

```bash
pip install folder-vision

# If command not found, run via module:
python -m folder_vision serve
```

## 🆕 What's New in v1.0.0

- ✅ **Auto-indexing**: Automatically indexes current directory
- ✅ **uv compatibility**: Perfect integration with uv tool management
- ✅ **Improved web UI**: Better search interface and gallery view
- ✅ **Image clustering**: Automatic grouping of similar images
- ✅ **Cross-platform**: Seamless installation on all platforms
- ✅ **No PATH issues**: Commands work immediately after install

## 📊 Performance Tips

### For Best Performance

1. **Use SSD storage** for image folders
2. **Close other apps** when indexing large collections  
3. **Use GPU** if available with `--device cuda`
4. **Index smaller folders** for faster startup

### Typical Performance

- **Small collections** (< 1000 images): Instant indexing
- **Medium collections** (1000-10000 images): 1-5 minutes  
- **Large collections** (10000+ images): 5-30 minutes

## 🤝 Support

- **Issues**: [GitHub Issues](https://github.com/folder-vision/folder-vision/issues)
- **Documentation**: Full docs in [README.md](README.md)
- **CLIP Model Info**: See [README_CLIP.md](README_CLIP.md)

## 📄 License

MIT License - use it anywhere, anytime!

---

**🎉 That's it! You're ready to search your images with AI.**

Made with ❤️ for the uv community
