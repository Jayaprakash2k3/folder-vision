# Folder Vision - CLIP Image Search 🔍

> The fastest way to search your images with AI - powered by OpenAI's CLIP model

**✨ Just point it at any folder and search your images using natural language!**

A powerful multimodal image search engine built with OpenAI's CLIP (Contrastive Language-Image Pre-training) model. Search through your image collections using natural language descriptions or find similar images using other images as queries.

## 🚀 Quick Start (2 minutes)

### 1. Install with uv (Recommended - fastest & easiest)

**Install uv first (if you don't have it):**

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Install Folder Vision:**

```bash
uv tool install folder-vision
```

### 2. Start Searching Your Images

```bash
# Navigate to any folder with images
cd ~/Pictures        # or ~/Desktop or any folder
cd /path/to/photos    # or wherever your images are

# Start the search engine
folder-vision serve
```

### 3. Open Your Browser

Go to `http://localhost:8000` and start searching with phrases like:

- "sunset over mountains"
- "cat sleeping on couch"
- "red sports car"
- "food on a plate"

### Alternative Installation Methods

**Using pipx (Second best option):**
```bash
pipx install folder-vision
folder-vision serve
```

**Using pip or manual installation:**
```bash
# Clone the repository
git clone https://github.com/Jayaprakash2k3/folder-vision.git
cd folder-vision

# Install dependencies
pip install -e .

# Start the web server
fv serve --port 8000
```

## Features ✨

- **🔍 Text-to-Image Search**: Find images using natural language descriptions
- **🖼️ Image-to-Image Search**: Find similar images using another image as a query
- **🌐 Web Interface**: Beautiful, intuitive web UI for easy searching
- **⚡ CLI Interface**: Command-line tools for batch processing and automation
- **💾 Smart Caching**: Automatic embedding caching for fast subsequent searches
- **🚀 FastAPI Backend**: Modern, high-performance web API
- **📱 Responsive Design**: Works on desktop, tablet, and mobile devices
- **🎯 Auto-Indexing**: Automatically indexes current directory
- **🔧 Cross-Platform**: Seamless installation on Windows, macOS, and Linux

## ✨ Why Use uv?

**uv** is the fastest Python package manager and handles everything automatically:

- ✅ **No PATH issues**: Commands work immediately after install
- ✅ **Isolated environment**: Doesn't conflict with other Python packages  
- ✅ **Cross-platform**: Same commands work on Windows, macOS, and Linux
- ✅ **Faster**: Installs packages 10-100x faster than pip
- ✅ **No virtual environment needed**: Handles isolation automatically

## � What You Can Do

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

## How It Works 🧠

Folder Vision uses OpenAI's CLIP model to understand both images and text in the same semantic space. This allows for:

1. **Image Indexing**: Convert all your images into high-dimensional vector embeddings
2. **Text Understanding**: Convert your search queries into comparable vectors
3. **Similarity Matching**: Find the most similar images using cosine similarity
4. **Fast Retrieval**: Use cached embeddings for instant search results

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

### Advanced CLI Commands

```bash
# Custom host and port
fv serve --host localhost --port 3000

# Development mode with auto-reload
fv serve --reload

# Index without saving cache
fv index /path/to/images --no-cache

# JSON output for scripting
fv search-text "dogs playing" --format json

# Bind to all interfaces
folder-vision serve --host 0.0.0.0 --port 8000

# Specify custom folder to index
folder-vision serve --index-dir /path/to/images
```

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

### Digital Asset Management
```bash
# Index product images
fv index /company/product_photos

# Find specific product types
fv search-text "red athletic shoes"
fv search-text "office furniture desk"
```

## Web Interface Features 🌐

The web interface provides:

- **📁 Folder Indexing**: Point to any folder and index all images automatically
- **🔤 Text Search**: Type natural language descriptions to find matching images
- **🖼️ Visual Search**: Upload an image to find similar ones in your collection
- **📊 Statistics**: View indexing statistics and model information
- **🎨 Visual Results**: See thumbnail previews with similarity scores
- **📱 Responsive Design**: Works perfectly on all devices

## API Endpoints 🔌

The FastAPI backend provides these endpoints:

- `GET /` - Web interface
- `POST /index` - Index a folder
- `GET /search/text` - Search by text query
- `POST /search/image` - Search by image upload
- `GET /image/{path}` - Serve image files
- `GET /stats` - Get statistics
- `GET /health` - Health check

## Supported Image Formats 📸

- JPEG (.jpg, .jpeg)
- PNG (.png)
- BMP (.bmp)
- GIF (.gif)
- TIFF (.tiff)
- WebP (.webp)

## Performance & Optimization ⚡

- **GPU Support**: Automatically uses GPU if available (CUDA)
- **Batch Processing**: Efficient batch encoding of images
- **Smart Caching**: Embeddings are cached to disk for instant reloading
- **Memory Management**: Processes large collections without memory issues
- **Concurrent Processing**: Handles multiple search requests simultaneously

### Typical Performance

- **Small collections** (< 1000 images): Instant indexing
- **Medium collections** (1000-10000 images): 1-5 minutes  
- **Large collections** (10000+ images): 5-30 minutes

### For Best Performance

1. **Use SSD storage** for image folders
2. **Close other apps** when indexing large collections  
3. **Use GPU** if available with `--device cuda`
4. **Index smaller folders** for faster startup

## ⚙️ System Requirements

- **Python**: 3.9+ (automatically handled by uv)
- **Memory**: 4GB+ recommended for large collections
- **Storage**: Additional space for embedding cache files
- **GPU**: Optional but recommended for faster processing (CUDA-compatible)
- **Images**: Supports JPG, PNG, GIF, BMP, TIFF, WebP
- **Internet**: Only needed for initial model download

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

### Common Issues

**"No images indexed" error**:
- Make sure to run `fv index <folder_path>` first
- Check that the folder contains supported image formats

**Slow indexing**:
- Enable GPU acceleration if available
- Process smaller batches of images
- Use SSD storage for better I/O performance

**Memory errors**:
- Reduce batch size in the code
- Process images in smaller folders
- Increase system RAM

**Web interface not loading**:
- Check if port is already in use
- Try a different port: `fv serve --port 8080`
- Check firewall settings

### For large image collections

```bash
# Index in chunks for better performance
folder-vision index /huge/folder --batch-size 100

# Use GPU if available (much faster)
folder-vision serve --device cuda
```

## Model Information 🤖

- **Base Model**: OpenAI CLIP ViT-B/32
- **Embedding Dimension**: 512
- **Input Resolution**: 224x224 pixels
- **Vocabulary**: 49,408 tokens

## Advanced Configuration ⚙️

### Environment Variables

```bash
# Set custom cache directory
export CLIP_CACHE_DIR=/path/to/cache

# Disable GPU usage
export CUDA_VISIBLE_DEVICES=""
```

### Custom Model

You can use different CLIP models by modifying the code:

```python
# In clip_search.py
search_engine = CLIPImageSearch(model_name="openai/clip-vit-large-patch14")
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

## Development 👩‍💻

### Project Structure
```
folder-vision/
├── folder_vision/
│   ├── __init__.py
│   ├── app.py           # FastAPI web application
│   ├── cli.py           # Command-line interface
│   └── clip_search.py   # CLIP search engine
├── requirements.txt     # Python dependencies
├── pyproject.toml      # Project configuration
└── README.md           # This file
```

### Running Tests
```bash
# Install development dependencies
pip install -e ".[dev]"

# Run tests
pytest tests/
```

### Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 🆕 What's New in v1.0.0

- ✅ **Auto-indexing**: Automatically indexes current directory
- ✅ **uv compatibility**: Perfect integration with uv tool management
- ✅ **Improved web UI**: Better search interface and gallery view
- ✅ **Image clustering**: Automatic grouping of similar images
- ✅ **Cross-platform**: Seamless installation on all platforms
- ✅ **No PATH issues**: Commands work immediately after install

## Support 💬

- **Issues**: [GitHub Issues](https://github.com/Jayaprakash2k3/folder-vision/issues)
- **Documentation**: Full docs in this README
- **Repository**: [GitHub Repository](https://github.com/Jayaprakash2k3/folder-vision/tree/main/folder-vision)

If you encounter any issues or have questions:

1. Check the troubleshooting section above
2. Search existing issues on GitHub
3. Create a new issue with detailed information
4. Include system information and error messages

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments 🙏

- **OpenAI** for the incredible CLIP model
- **Hugging Face** for the transformers library
- **FastAPI** for the excellent web framework
- **PyTorch** for the deep learning foundation

---

**🎉 That's it! You're ready to search your images with AI.**

**Made with ❤️ for the uv community and image search enthusiasts**

Start exploring your images in a whole new way! 🚀

### Command Line Usage

Index your images:

```bash
fv index /path/to/your/images
```

Search with text:

```bash
fv search-text "a red car in the city"
```

Search with an image:

```bash
fv search-image /path/to/query_image.jpg
```

## How It Works 🧠

Folder Vision uses OpenAI's CLIP model to understand both images and text in the same semantic space. This allows for:

1. **Image Indexing**: Convert all your images into high-dimensional vector embeddings
2. **Text Understanding**: Convert your search queries into comparable vectors
3. **Similarity Matching**: Find the most similar images using cosine similarity
4. **Fast Retrieval**: Use cached embeddings for instant search results

## Web Interface Features 🌐

The web interface provides:

- **📁 Folder Indexing**: Point to any folder and index all images automatically
- **🔤 Text Search**: Type natural language descriptions to find matching images
- **🖼️ Visual Search**: Upload an image to find similar ones in your collection
- **📊 Statistics**: View indexing statistics and model information
- **🎨 Visual Results**: See thumbnail previews with similarity scores
- **📱 Responsive Design**: Works perfectly on all devices

## CLI Commands 💻

### Serve Web Interface
```bash
# Start web server (default: http://0.0.0.0:8000)
fv serve

# Custom host and port
fv serve --host localhost --port 3000

# Development mode with auto-reload
fv serve --reload
```

### Index Images
```bash
# Index all images in a folder
fv index /path/to/images

# Index without saving cache
fv index /path/to/images --no-cache
```

### Search Commands
```bash
# Text search (natural language)
fv search-text "sunset over mountains"
fv search-text "a cat sleeping on a couch" --top-k 5

# Image search (visual similarity)
fv search-image /path/to/query.jpg
fv search-image query.png --top-k 20

# JSON output for scripting
fv search-text "dogs playing" --format json
```

### Statistics
```bash
# View search engine statistics
fv stats
```

## API Endpoints 🔌

The FastAPI backend provides these endpoints:

- `GET /` - Web interface
- `POST /index` - Index a folder
- `GET /search/text` - Search by text query
- `POST /search/image` - Search by image upload
- `GET /image/{path}` - Serve image files
- `GET /stats` - Get statistics
- `GET /health` - Health check

## Supported Image Formats 📸

- JPEG (.jpg, .jpeg)
- PNG (.png)
- BMP (.bmp)
- GIF (.gif)
- TIFF (.tiff)
- WebP (.webp)

## Performance & Optimization ⚡

- **GPU Support**: Automatically uses GPU if available (CUDA)
- **Batch Processing**: Efficient batch encoding of images
- **Smart Caching**: Embeddings are cached to disk for instant reloading
- **Memory Management**: Processes large collections without memory issues
- **Concurrent Processing**: Handles multiple search requests simultaneously

## Example Use Cases 💡

### Personal Photo Management
```bash
# Index your photo library
fv index ~/Pictures

# Find vacation photos
fv search-text "beach vacation sunset"

# Find similar photos to a favorite shot
fv search-image ~/Pictures/favorite_sunset.jpg
```

### Digital Asset Management
```bash
# Index product images
fv index /company/product_photos

# Find specific product types
fv search-text "red athletic shoes"
fv search-text "office furniture desk"
```

### Creative Workflows
```bash
# Index design assets
fv index /projects/design_assets

# Find inspiration
fv search-text "minimalist logo design"
fv search-text "modern interior architecture"
```

## System Requirements 🖥️

- **Python**: 3.9 or higher
- **Memory**: 4GB RAM minimum, 8GB+ recommended for large collections
- **Storage**: Additional space for embedding cache files
- **GPU**: Optional but recommended for faster processing (CUDA-compatible)

## Model Information 🤖

- **Base Model**: OpenAI CLIP ViT-B/32
- **Embedding Dimension**: 512
- **Input Resolution**: 224x224 pixels
- **Vocabulary**: 49,408 tokens

## Advanced Configuration ⚙️

### Environment Variables

```bash
# Set custom cache directory
export CLIP_CACHE_DIR=/path/to/cache

# Disable GPU usage
export CUDA_VISIBLE_DEVICES=""
```

### Custom Model

You can use different CLIP models by modifying the code:

```python
# In clip_search.py
search_engine = CLIPImageSearch(model_name="openai/clip-vit-large-patch14")
```

## Troubleshooting 🔧

### Common Issues

**"No images indexed" error**:
- Make sure to run `fv index <folder_path>` first
- Check that the folder contains supported image formats

**Slow indexing**:
- Enable GPU acceleration if available
- Process smaller batches of images
- Use SSD storage for better I/O performance

**Memory errors**:
- Reduce batch size in the code
- Process images in smaller folders
- Increase system RAM

**Web interface not loading**:
- Check if port is already in use
- Try a different port: `fv serve --port 8080`
- Check firewall settings

## Development 👩‍💻

### Project Structure
```
folder-vision/
├── folder_vision/
│   ├── __init__.py
│   ├── app.py           # FastAPI web application
│   ├── cli.py           # Command-line interface
│   └── clip_search.py   # CLIP search engine
├── requirements.txt     # Python dependencies
├── pyproject.toml      # Project configuration
└── README.md           # This file
```

### Running Tests
```bash
# Install development dependencies
pip install -e ".[dev]"

# Run tests
pytest tests/
```

### Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments 🙏

- **OpenAI** for the incredible CLIP model
- **Hugging Face** for the transformers library
- **FastAPI** for the excellent web framework
- **PyTorch** for the deep learning foundation

## Support 💬

If you encounter any issues or have questions:

1. Check the troubleshooting section above
2. Search existing issues on GitHub
3. Create a new issue with detailed information
4. Include system information and error messages

---

**Made with ❤️ by the Folder Vision Team**

Start exploring your images in a whole new way! 🚀