#!/usr/bin/env python3
"""
Setup script to ensure folder-vision command is available after pip install.
Run this after 'pip install folder-vision' if you get "command not found".

Usage: python setup_path.py
"""
import os
import sys
import sysconfig
import subprocess
from pathlib import Path


def get_scripts_dir():
    """Get the directory where pip installs console scripts."""
    if hasattr(sysconfig, 'get_paths'):
        return sysconfig.get_paths()['scripts']
    else:
        # Fallback for older Python
        return sysconfig.get_path('scripts')


def is_on_path(directory):
    """Check if directory is on PATH."""
    path_dirs = os.environ.get('PATH', '').split(os.pathsep)
    return directory in path_dirs


def get_shell_config_file():
    """Determine which shell config file to update."""
    shell = os.environ.get('SHELL', '').split('/')[-1]
    home = Path.home()
    
    if shell == 'zsh':
        return home / '.zshrc'
    elif shell == 'bash':
        if sys.platform == 'darwin':  # macOS
            return home / '.bash_profile'
        else:  # Linux
            return home / '.bashrc'
    elif shell == 'fish':
        return home / '.config' / 'fish' / 'config.fish'
    else:
        # Default to .bashrc
        return home / '.bashrc'


def add_to_path_unix(scripts_dir):
    """Add scripts directory to PATH on Unix-like systems."""
    config_file = get_shell_config_file()
    
    # Read existing content
    if config_file.exists():
        content = config_file.read_text()
    else:
        content = ""
    
    # Check if already added
    path_line = f'export PATH="{scripts_dir}:$PATH"'
    if scripts_dir in content:
        print(f"✓ {scripts_dir} appears to already be in {config_file}")
        return
    
    # Add to config file
    with open(config_file, 'a') as f:
        f.write(f'\n# Added by folder-vision setup\n')
        f.write(f'{path_line}\n')
    
    print(f"✓ Added {scripts_dir} to {config_file}")
    print(f"ℹ️  Restart your terminal or run: source {config_file}")


def add_to_path_windows(scripts_dir):
    """Add scripts directory to PATH on Windows."""
    try:
        import winreg
        
        # Open the Environment key
        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r'Environment',
            0,
            winreg.KEY_ALL_ACCESS
        )
        
        try:
            # Get current PATH
            current_path, _ = winreg.QueryValueEx(key, 'PATH')
        except FileNotFoundError:
            current_path = ""
        
        # Check if already in PATH
        if scripts_dir.lower() in current_path.lower():
            print(f"✓ {scripts_dir} is already in PATH")
            return
        
        # Add to PATH
        new_path = f"{scripts_dir};{current_path}" if current_path else scripts_dir
        winreg.SetValueEx(key, 'PATH', 0, winreg.REG_EXPAND_SZ, new_path)
        winreg.CloseKey(key)
        
        print(f"✓ Added {scripts_dir} to PATH")
        print("ℹ️  Restart your command prompt/PowerShell for changes to take effect")
        
    except ImportError:
        print("❌ Could not modify PATH automatically on Windows")
        print(f"ℹ️  Manually add this to your PATH: {scripts_dir}")


def main():
    print("🔧 folder-vision PATH setup")
    print("=" * 40)
    
    # Get scripts directory
    scripts_dir = get_scripts_dir()
    print(f"📁 Scripts directory: {scripts_dir}")
    
    # Check if folder-vision exists
    if sys.platform == 'win32':
        script_path = Path(scripts_dir) / 'folder-vision.exe'
    else:
        script_path = Path(scripts_dir) / 'folder-vision'
    
    if not script_path.exists():
        print("❌ folder-vision not found. Make sure you've run 'pip install folder-vision' first.")
        return 1
    
    print(f"✓ Found folder-vision at: {script_path}")
    
    # Check if on PATH
    if is_on_path(scripts_dir):
        print("✓ Scripts directory is already on PATH")
        
        # Test the command
        try:
            result = subprocess.run(['folder-vision', '--version'], 
                                  capture_output=True, text=True, timeout=5)
            if result.returncode == 0:
                print("✓ folder-vision command works!")
                print(f"Version: {result.stdout.strip()}")
                return 0
        except (subprocess.TimeoutExpired, FileNotFoundError):
            pass
    
    print("⚠️  Scripts directory not on PATH or command not working")
    
    # Add to PATH
    if sys.platform == 'win32':
        add_to_path_windows(scripts_dir)
    else:
        add_to_path_unix(scripts_dir)
    
    print("\n🚀 Setup complete!")
    print("\nAlternatives if the command still doesn't work:")
    print("  1. Run: python -m folder_vision")
    print("  2. Use pipx: pipx install folder-vision")
    print(f"  3. Run directly: {script_path}")
    
    return 0


if __name__ == '__main__':
    sys.exit(main())