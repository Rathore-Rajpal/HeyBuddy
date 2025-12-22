"""
Build script for creating Buddy installer
Creates a standalone executable using PyInstaller
"""

import os
import sys
import shutil
import subprocess

def clean_build():
    """Clean previous build artifacts"""
    print("Cleaning previous builds...")
    dirs_to_remove = ['build', 'dist', '__pycache__']
    for d in dirs_to_remove:
        if os.path.exists(d):
            shutil.rmtree(d)
            print(f"  Removed {d}/")
    
    if os.path.exists('Buddy.spec'):
        os.remove('Buddy.spec')
        print("  Removed Buddy.spec")

def check_pyinstaller():
    """Check if PyInstaller is installed"""
    try:
        import PyInstaller
        print(f"PyInstaller version: {PyInstaller.__version__}")
        return True
    except ImportError:
        print("PyInstaller not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
        return True

def create_spec_file():
    """Create PyInstaller spec file"""
    spec_content = """# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

# Collect all data files
datas = [
    ('assist', 'assist'),
    ('*.bat', '.'),
    ('*.md', '.'),
    ('.env.example', '.'),
]

# Hidden imports that PyInstaller might miss
hiddenimports = [
    'bottle',
    'eel',
    'pywhatkit',
    'pyttsx3',
    'cv2',
    'mediapipe',
    'numpy',
    'requests',
    'Pillow',
    'PyAutoGUI',
    'wikipedia',
    'pvporcupine',
    'pyaudio',
    'sounddevice',
    'google.generativeai',
    'dotenv',
]

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Buddy',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,  # Set to False to hide console window
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='assist/www/assets/img/icon.ico' if os.path.exists('assist/www/assets/img/icon.ico') else None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Buddy',
)
"""
    
    with open('Buddy.spec', 'w') as f:
        f.write(spec_content)
    print("Created Buddy.spec")

def build_exe():
    """Build the executable"""
    print("\nBuilding executable with PyInstaller...")
    print("This may take several minutes...\n")
    
    subprocess.check_call([
        'pyinstaller',
        '--clean',
        'Buddy.spec'
    ])
    
    print("\n✓ Build complete!")

def create_readme():
    """Create README for distribution"""
    readme = """# Buddy - AI Desktop Assistant

## Installation

1. Extract all files to a folder (e.g., C:\\Program Files\\Buddy)
2. Run Buddy.exe
3. Follow the first-time setup wizard:
   - Enter your name
   - (Optional) Configure face authentication
   - (Optional) Add API keys for advanced features

## Requirements

- Windows 10/11
- Webcam (for face authentication and virtual mouse)
- Microphone (for voice commands)

## Features

- 🎤 Voice-activated assistant with wake word "Buddy"
- 🖱️ Air gesture mouse control
- 🎵 Spotify integration
- 🤖 AI image generation
- 💬 AI chat assistant
- 🎭 Facial recognition authentication

## Configuration

### API Keys (Optional)

To enable all features, you'll need:

1. **Spotify API** (for music control)
   - Get from: https://developer.spotify.com/dashboard
   - Required: Client ID and Client Secret

2. **HuggingFace API** (for AI image generation)
   - Get from: https://huggingface.co/settings/tokens
   - Required: API Token

You can add these during first-time setup or later in the .env file.

## Troubleshooting

**Face authentication not working:**
- Ensure webcam is connected
- Check webcam permissions in Windows Settings
- Try reconfiguring face auth in settings

**Voice commands not recognized:**
- Check microphone permissions
- Ensure microphone is set as default in Windows
- Say the wake word "Buddy" clearly

**Spotify not working:**
- Verify API credentials in .env file
- Ensure Spotify app is installed and running
- Check internet connection

## Support

For issues and questions:
- GitHub: https://github.com/Rathore-Rajpal/HeyBuddy
- Issues: https://github.com/Rathore-Rajpal/HeyBuddy/issues

## License

This project is licensed under the MIT License.
"""
    
    with open('dist/Buddy/README.txt', 'w') as f:
        f.write(readme)
    print("Created distribution README")

def create_installer():
    """Create installer using Inno Setup (if available)"""
    print("\nTo create a Windows installer:")
    print("1. Install Inno Setup: https://jrsoftware.org/isdl.php")
    print("2. Create installer script (see RELEASE_GUIDE.md)")
    print("3. Or distribute the dist/Buddy folder as a .zip file")

def main():
    """Main build process"""
    print("=" * 60)
    print("Buddy - Build Installer")
    print("=" * 60)
    print()
    
    # Check PyInstaller
    if not check_pyinstaller():
        print("Failed to install PyInstaller")
        return
    
    # Clean previous builds
    clean_build()
    
    # Create spec file
    create_spec_file()
    
    # Build executable
    try:
        build_exe()
    except subprocess.CalledProcessError as e:
        print(f"\n✗ Build failed: {e}")
        return
    
    # Create distribution files
    create_readme()
    
    # Copy .env.example
    if os.path.exists('.env.example'):
        shutil.copy('.env.example', 'dist/Buddy/.env.example')
        print("Copied .env.example to distribution")
    
    print("\n" + "=" * 60)
    print("Build Summary")
    print("=" * 60)
    print(f"Output folder: dist/Buddy/")
    print(f"Executable: dist/Buddy/Buddy.exe")
    print(f"Size: {get_folder_size('dist/Buddy'):.1f} MB")
    print()
    print("Next steps:")
    print("1. Test the executable: dist/Buddy/Buddy.exe")
    print("2. Create a .zip file for distribution")
    print("3. (Optional) Create installer with Inno Setup")
    print("4. Upload to GitHub Releases")
    print()
    create_installer()

def get_folder_size(folder):
    """Get total size of folder in MB"""
    total = 0
    for dirpath, dirnames, filenames in os.walk(folder):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if os.path.exists(fp):
                total += os.path.getsize(fp)
    return total / (1024 * 1024)

if __name__ == '__main__':
    main()
