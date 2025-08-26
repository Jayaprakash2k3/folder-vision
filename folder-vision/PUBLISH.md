# Publishing to PyPI Instructions

## Prerequisites
1. Create accounts on:
   - TestPyPI: https://test.pypi.org/account/register/
   - PyPI: https://pypi.org/account/register/

2. Generate API tokens:
   - TestPyPI: https://test.pypi.org/manage/account/token/
   - PyPI: https://pypi.org/manage/account/token/

## Configure credentials
Create `~/.pypirc`:
```ini
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
repository = https://upload.pypi.org/legacy/
username = __token__
password = pypi-YOUR_REAL_TOKEN_HERE

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi-YOUR_TEST_TOKEN_HERE
```

## Upload commands
```bash
# Test first
twine upload --repository testpypi dist/*

# If test works, upload to real PyPI
twine upload dist/*
```

## Verify installation
```bash
# From TestPyPI
pip install -i https://test.pypi.org/simple/ folder-vision==0.1.0

# From real PyPI (after publishing)
pip install folder-vision
```