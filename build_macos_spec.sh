#!/bin/bash

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

# Build the Windows executable with the spec file directly
echo "Building executable with PyInstaller spec file..."
pyinstaller gui.spec --noconfirm

echo "Build completed. Check the 'dist' directory for the executable."

# Deactivate the virtual environment
deactivate 