#!/bin/bash
################################################################################
# MLOps Assignment 2 - Integrated Setup Script
# This script sets up the complete environment for all platforms
################################################################################

set -e  # Exit on any error

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Function to print headers
print_header() {
    echo ""
    echo -e "${BLUE}========================================${NC}"
    echo -e "${BLUE}$1${NC}"
    echo -e "${BLUE}========================================${NC}"
    echo ""
}

# Function to print success messages
print_success() {
    echo -e "${GREEN}✓${NC} $1"
}

# Function to print info messages
print_info() {
    echo -e "${BLUE}→${NC} $1"
}

# Function to print warning messages
print_warning() {
    echo -e "${YELLOW}⚠${NC} $1"
}

# Function to print error messages
print_error() {
    echo -e "${RED}✗${NC} $1"
}

# Detect OS and Python version
print_header "System Detection"

OS_TYPE=$(uname -s)
PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')

print_info "Operating System: $OS_TYPE"
print_info "Python Version: $PYTHON_VERSION"

# Check Python version (need 3.8+)
PYTHON_MINOR=$(python3 -c 'import sys; print(sys.version_info[1])')
if [ "$PYTHON_MINOR" -lt 8 ]; then
    print_error "Python 3.8+ required, but found 3.$PYTHON_MINOR"
    exit 1
fi
print_success "Python version compatible"

# Detect platform and set requirements file
print_header "Platform Configuration"

if [[ "$OS_TYPE" == "Linux" ]]; then
    REQUIREMENTS_FILE="requirements-rocky-linux.txt"
    print_info "Detected Linux (Rocky/CentOS compatible)"
    print_info "Using: $REQUIREMENTS_FILE"
elif [[ "$OS_TYPE" == "Darwin" ]]; then
    REQUIREMENTS_FILE="requirements.txt"
    print_info "Detected macOS"
    print_info "Using: $REQUIREMENTS_FILE"
else
    REQUIREMENTS_FILE="requirements.txt"
    print_warning "Unknown OS, using default requirements.txt"
fi

# Check if requirements file exists
if [ ! -f "$REQUIREMENTS_FILE" ]; then
    print_error "$REQUIREMENTS_FILE not found!"
    exit 1
fi
print_success "Requirements file found: $REQUIREMENTS_FILE"

# Create virtual environment
print_header "Virtual Environment Setup"

if [ -d "venv" ]; then
    print_warning "Virtual environment already exists"
    read -p "Do you want to recreate it? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        print_info "Removing existing virtual environment..."
        rm -rf venv
        python3 -m venv venv
        print_success "Virtual environment created"
    else
        print_info "Using existing virtual environment"
    fi
else
    print_info "Creating virtual environment..."
    python3 -m venv venv
    print_success "Virtual environment created"
fi

# Activate virtual environment
print_info "Activating virtual environment..."
source venv/bin/activate
print_success "Virtual environment activated"

# Upgrade pip, setuptools, wheel
print_header "Upgrading Package Manager Tools"

print_info "Upgrading pip, setuptools, wheel..."
pip install --upgrade pip setuptools wheel > /dev/null 2>&1
print_success "Package manager tools upgraded"

# Install dependencies
print_header "Installing Dependencies"

print_info "Installing from $REQUIREMENTS_FILE..."
print_info "(This may take a few minutes...)"
echo ""

if pip install -r "$REQUIREMENTS_FILE"; then
    print_success "All dependencies installed successfully"
else
    print_error "Failed to install dependencies"
    exit 1
fi

# Verify critical packages
print_header "Verifying Installation"

PACKAGES=("pandas" "numpy" "openai" "mlflow" "jupyter")
INSTALL_COUNT=0

for package in "${PACKAGES[@]}"; do
    if python3 -c "import $package" 2>/dev/null; then
        VERSION=$(python3 -c "import $package; print(getattr($package, '__version__', 'unknown'))" 2>/dev/null)
        print_success "$package ($VERSION)"
        ((INSTALL_COUNT++))
    else
        print_error "$package - NOT INSTALLED"
    fi
done

if [ "$INSTALL_COUNT" -lt ${#PACKAGES[@]} ]; then
    print_error "Some packages failed to install"
    exit 1
fi

# Setup .env file
print_header "Configuration Setup"

if [ ! -f ".env" ]; then
    if [ -f ".env.example" ]; then
        print_info "Creating .env from .env.example..."
        cp .env.example .env
        print_success ".env file created"
        print_warning "Please edit .env and add your OPENAI_API_KEY"
    else
        print_error ".env.example not found"
        exit 1
    fi
else
    print_info ".env file already exists"
    if grep -q "OPENAI_API_KEY=sk-" .env; then
        print_success ".env file has valid API key configured"
    else
        print_warning "API key in .env may not be configured correctly"
        print_info "Please edit .env and ensure OPENAI_API_KEY is set"
    fi
fi

# Create necessary directories
print_header "Creating Project Directories"

DIRS=("data" "outputs" "screenshots" "mlruns")
for dir in "${DIRS[@]}"; do
    if [ ! -d "$dir" ]; then
        mkdir -p "$dir"
        print_success "Created $dir/"
    else
        print_info "$dir/ already exists"
    fi
done

# Summary
print_header "Setup Complete!"

echo -e "${GREEN}✓ Environment is ready!${NC}"
echo ""
echo "Quick Start:"
echo "  1. Activate environment (if not already active):"
echo -e "     ${BLUE}source ./activate.sh${NC}"
echo ""
echo "  2. Run verification:"
echo -e "     ${BLUE}bash verify_setup.sh${NC}"
echo ""
echo "  3. Start the notebook:"
echo -e "     ${BLUE}jupyter notebook llmops_assignment.ipynb${NC}"
echo ""
echo "View MLflow Results:"
echo -e "     ${BLUE}mlflow ui --port 5000${NC}"
echo ""
echo "For detailed setup guide, see: ROCKY_LINUX_SETUP.md"
echo "For quick reference, see: QUICK_START.md"
echo ""
