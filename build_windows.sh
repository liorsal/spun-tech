#!/bin/bash

# Build the Docker image
echo "Building Docker image..."
docker build --platform linux/amd64 -t pyinstaller-wine-builder -f dockerfile .

# Run the Docker container to create the Windows executable
echo "Creating Windows executable..."
docker run --rm -v "$(pwd):/app" pyinstaller-wine-builder

echo "Build completed. Check the 'dist' directory for gui.exe" 