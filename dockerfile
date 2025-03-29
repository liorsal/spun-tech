FROM --platform=linux/amd64 ubuntu:20.04

# Avoid prompts from apt
ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    python3 python3-pip python3-dev \
    wine64 \
    && rm -rf /var/lib/apt/lists/*

# Set up a working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip3 install -r requirements.txt
RUN pip3 install pyinstaller

# Copy application files
COPY . /app/

# Create Windows executable
CMD ["wine64", "python", "-m", "PyInstaller", "--onefile", "--windowed", "gui.py"]