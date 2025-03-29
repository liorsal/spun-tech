#!/bin/bash

# Check if Homebrew is installed
if ! command -v brew &> /dev/null; then
    echo "Homebrew is not installed. Installing Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
fi

# Install Wine if not installed
if ! command -v wine &> /dev/null; then
    echo "Wine is not installed. Installing Wine..."
    brew install --cask wine-stable
fi

# Create a virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating Python virtual environment..."
    python3 -m venv venv
fi

# Activate the virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install the required packages
echo "Installing Python packages..."
pip install -r requirements.txt
pip install pyinstaller

# Build the Windows executable
echo "Building Windows executable..."
pyinstaller --onefile --windowed gui.py

echo "Build completed. Check the 'dist' directory for gui.exe"

# Deactivate the virtual environment
deactivate 