# Publishing Guide for Folder Vision

This document outlines how to publish the folder-vision package to PyPI so that users can install it with `uv`, `pip`, or `pipx`.

## Prerequisites

1. **PyPI Account**: Create an account at https://pypi.org
2. **Test PyPI Account**: Create an account at https://test.pypi.org (for testing)
3. **API Tokens**: Generate API tokens for both PyPI and Test PyPI

## Package Structure

The package is now properly structured with:
- All Python code in `folder_vision/` directory
- HTML templates in `folder_vision/html/`
- Static assets in `folder_vision/static/`
- Proper `pyproject.toml` configuration
- MANIFEST.in for additional file inclusion

## Building the Package

The package has been built and is ready for distribution:

```bash
# Clean previous builds
rm -rf dist/ build/ *.egg-info

# Build the package
python3 -m build
```

This creates:
- `dist/folder_vision-1.0.0.tar.gz` (source distribution)
- `dist/folder_vision-1.0.0-py3-none-any.whl` (wheel distribution)

## Testing the Package Locally

Before publishing, test the package locally:

```bash
# Install in a virtual environment
python3 -m venv test_env
source test_env/bin/activate  # On Windows: test_env\Scripts\activate

# Install from local wheel
pip install dist/folder_vision-1.0.0-py3-none-any.whl

# Test the installation
folder-vision --help
cd /path/to/images
folder-vision serve --port 8001

# Clean up
deactivate
rm -rf test_env
```

## Publishing to Test PyPI (Recommended First Step)

1. **Install twine**:
   ```bash
   pip install twine
   ```

2. **Upload to Test PyPI**:
   ```bash
   twine upload --repository testpypi dist/*
   ```

3. **Test installation from Test PyPI**:
   ```bash
   pip install --index-url https://test.pypi.org/simple/ folder-vision
   ```

## Publishing to PyPI

Once testing is complete:

```bash
# Upload to PyPI
twine upload dist/*
```

## Installation Methods for Users

After publishing, users can install using:

### Method 1: uv (Recommended)
```bash
# Install uv if not already installed
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install folder-vision
uv tool install folder-vision

# Use it
cd /path/to/images
folder-vision serve
```

### Method 2: pipx (Isolated Installation)
```bash
pipx install folder-vision
folder-vision serve
```

### Method 3: pip
```bash
pip install folder-vision
folder-vision serve
```

### Method 4: Direct Module Execution
```bash
pip install folder-vision
python -m folder_vision serve
```

## Version Management

To release a new version:

1. Update the version in `pyproject.toml`:
   ```toml
   version = "1.0.1"
   ```

2. Rebuild and republish:
   ```bash
   rm -rf dist/ build/ *.egg-info
   python3 -m build
   twine upload dist/*
   ```

## GitHub Release

Consider creating a GitHub release with the built artifacts:

1. Tag the release: `git tag v1.0.0`
2. Push the tag: `git push origin v1.0.0`
3. Create a release on GitHub and attach the dist files

## Package Features

The published package includes:
- ✅ Cross-platform CLI tools (`folder-vision` and `fv` commands)
- ✅ Complete web interface with HTML templates and CSS/JS assets
- ✅ Automatic directory indexing
- ✅ CLIP-powered image search
- ✅ Image clustering and visualization
- ✅ Gallery view with pagination
- ✅ All dependencies properly specified

## Troubleshooting

**Permission Errors**: Use `--user` flag with pip or use virtual environments

**Command Not Found**: Ensure Python scripts directory is in PATH, or use pipx/uv

**Import Errors**: All dependencies are specified in pyproject.toml and will be installed automatically

## Support

Users can:
- Install with uv: `uv tool install folder-vision`
- Run from any directory with images
- Access the web interface at http://localhost:8000
- Use CLI commands for batch operations

The package is now ready for production use and distribution!