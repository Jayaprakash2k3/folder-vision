@echo off
REM Windows installer script for folder-vision
echo Installing folder-vision...
pip install folder-vision
if %errorlevel% neq 0 (
    echo Failed to install folder-vision
    pause
    exit /b 1
)

echo.
echo Testing installation...
folder-vision --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Installation successful but command not on PATH
    echo Running setup helper...
    python setup_path.py
    echo.
    echo You can also run: python -m folder_vision
) else (
    echo Installation successful!
    echo You can run: folder-vision
)

echo.
echo Starting folder-vision server on port 8000...
echo Press Ctrl+C to stop the server
echo.
python -m folder_vision
pause