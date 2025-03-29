# Building Windows Executable for Flask Digital Form

Due to compatibility issues with cross-compiling from macOS to Windows (especially on Apple Silicon Macs), the recommended approach is to build the Windows executable on a Windows machine/VM or use a cloud-based Windows build service.

## Option 1: Build on a Windows Machine or VM

1. **Set up a Windows environment:**
   - Use a Windows machine, or
   - Set up a Windows VM using VirtualBox, Parallels, or VMware on your Mac
   - You can also use a cloud-based Windows VM (Azure, AWS, etc.)

2. **Install Python on Windows:**
   - Download and install Python 3.9 from https://www.python.org/downloads/
   - Make sure to check "Add Python to PATH" during installation

3. **Copy your project files to the Windows machine**

4. **Open Command Prompt on Windows and navigate to your project directory:**
   ```
   cd path\to\your\project
   ```

5. **Create a virtual environment:**
   ```
   python -m venv venv
   venv\Scripts\activate
   ```

6. **Install dependencies:**
   ```
   pip install -r requirements.txt
   pip install pyinstaller
   ```

7. **Build the executable:**
   ```
   pyinstaller --onefile --windowed gui.py
   ```

8. **The executable will be in the `dist` folder**

## Option 2: Use Nuitka (Recommended)

Nuitka is an alternative to PyInstaller that often works better for complex applications.

1. **Install Python on Windows (as described above)**

2. **Install Nuitka and dependencies:**
   ```
   pip install nuitka
   pip install -r requirements.txt
   ```

3. **Build the executable using Nuitka:**
   ```
   python -m nuitka --follow-imports --standalone --windows-disable-console gui.py
   ```

4. **The executable will be created in the `gui.dist` directory**

## Option 3: Use a Cloud-Based Build Service

Several cloud-based services can build Windows executables for you:

1. **GitHub Actions:**
   - Create a GitHub repository for your code
   - Set up a GitHub Actions workflow to build a Windows executable
   - The workflow can use PyInstaller or Nuitka to create the executable
   - You can download the executable as an artifact after the workflow completes

2. **AppVeyor:**
   - AppVeyor is a CI/CD service with good Windows support
   - Set up an AppVeyor configuration to build your executable
   - Download the executable after the build completes

## Notes on Using the Windows Executable

- The Windows executable will need to be run on a Windows machine
- Make sure all required data files (templates, etc.) are included
- Test the executable thoroughly on a Windows machine before distribution 