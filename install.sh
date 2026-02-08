#!/bin/bash

# Installation script for Linux Package Installer
# This script sets up the application and creates a desktop entry

set -e

echo "======================================"
echo "Linux Package Installer - Setup"
echo "======================================"
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed."
    echo "Please install Python 3.6 or higher and try again."
    exit 1
fi

echo "✓ Python 3 found: $(python3 --version)"

# Check if python3-venv is installed
if ! python3 -m venv --help &> /dev/null; then
    echo "⚠ Warning: python3-venv is not installed."
    echo "Installing python3-venv..."
    
    # Try to install venv based on distribution
    if command -v apt &> /dev/null; then
        sudo apt update && sudo apt install -y python3-venv
    elif command -v dnf &> /dev/null; then
        sudo dnf install -y python3-venv
    elif command -v yum &> /dev/null; then
        sudo yum install -y python3-venv
    elif command -v pacman &> /dev/null; then
        sudo pacman -S python-virtualenv
    else
        echo "Error: Could not install python3-venv automatically."
        echo "Please install it manually for your distribution."
        exit 1
    fi
fi

echo "✓ python3-venv available"

# Get the current directory
INSTALL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Create virtual environment
VENV_DIR="$INSTALL_DIR/venv"
echo ""
echo "Creating virtual environment..."

if [ -d "$VENV_DIR" ]; then
    echo "⚠ Virtual environment already exists, recreating..."
    rm -rf "$VENV_DIR"
fi

python3 -m venv "$VENV_DIR"

if [ $? -eq 0 ]; then
    echo "✓ Virtual environment created at: $VENV_DIR"
else
    echo "✗ Failed to create virtual environment"
    exit 1
fi

# Activate virtual environment and install dependencies
echo ""
echo "Installing Python dependencies in virtual environment..."

# Use the venv's pip directly
"$VENV_DIR/bin/pip" install --upgrade pip
"$VENV_DIR/bin/pip" install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✓ Dependencies installed successfully"
else
    echo "✗ Failed to install dependencies"
    exit 1
fi

# Make main.py executable
chmod +x main.py
echo "✓ Made main.py executable"

# Create desktop entry
DESKTOP_FILE="$HOME/.local/share/applications/linux-package-installer.desktop"
mkdir -p "$HOME/.local/share/applications"

echo ""
echo "Creating desktop entry..."

cat > "$DESKTOP_FILE" << EOF
[Desktop Entry]
Name=Linux Package Installer
Comment=Install .deb and .rpm packages easily
Exec="$VENV_DIR/bin/python" "$INSTALL_DIR/main.py"
Icon=package-x-generic
Terminal=false
Type=Application
Categories=System;PackageManager;
EOF

if [ $? -eq 0 ]; then
    chmod +x "$DESKTOP_FILE"
    echo "✓ Desktop entry created at: $DESKTOP_FILE"
else
    echo "✗ Failed to create desktop entry"
fi

# Create a launcher script in user's bin directory
BIN_DIR="$HOME/.local/bin"
mkdir -p "$BIN_DIR"

LAUNCHER="$BIN_DIR/linux-package-installer"

cat > "$LAUNCHER" << EOF
#!/bin/bash
cd "$INSTALL_DIR"
"$VENV_DIR/bin/python" main.py "\$@"
EOF

chmod +x "$LAUNCHER"
echo "✓ Created launcher script at: $LAUNCHER"

# Check if .local/bin is in PATH
if [[ ":$PATH:" != *":$BIN_DIR:"* ]]; then
    echo ""
    echo "⚠ Warning: $BIN_DIR is not in your PATH"
    echo "Add the following line to your ~/.bashrc or ~/.zshrc:"
    echo "    export PATH=\"\$HOME/.local/bin:\$PATH\""
fi

echo ""
echo "======================================"
echo "Installation Complete!"
echo "======================================"
echo ""
echo "You can now run the application by:"
echo "  1. Running: $VENV_DIR/bin/python $INSTALL_DIR/main.py"
echo "  2. Running: linux-package-installer (if ~/.local/bin is in PATH)"
echo "  3. Searching for 'Linux Package Installer' in your application menu"
echo ""
echo "Note: The application uses a virtual environment at: $VENV_DIR"
echo ""
echo "Enjoy using Linux Package Installer!"
echo ""
