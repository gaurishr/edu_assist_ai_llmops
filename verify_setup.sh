#!/bin/bash
# Verification script for MLOps Assignment 2 setup
# Run this script after installation to verify everything is configured correctly

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo "=========================================="
echo "MLOps Assignment 2 - Verification Check"
echo "=========================================="
echo ""

# Counter for checks
PASSED=0
FAILED=0
WARNINGS=0

# Function to check if command exists
check_command() {
    if command -v "$1" &> /dev/null || type "$1" &> /dev/null; then
        echo -e "${GREEN}✓${NC} $2"
        ((PASSED++))
    else
        echo -e "${RED}✗${NC} $2"
        ((FAILED++))
    fi
}

# Function to check Python package
check_package() {
    local pkg_name="$1"
    local import_name="${2:-$1}"  # Use different import name if provided
    
    if python3 -c "import $import_name" 2>/dev/null; then
        version=$(python3 -c "import $import_name; print(getattr($import_name, '__version__', 'unknown'))" 2>/dev/null)
        echo -e "${GREEN}✓${NC} $pkg_name ($version)"
        ((PASSED++))
    else
        echo -e "${RED}✗${NC} $pkg_name - NOT INSTALLED"
        ((FAILED++))
    fi
}

# Function to check file exists
check_file() {
    if [ -f "$1" ]; then
        echo -e "${GREEN}✓${NC} $2"
        ((PASSED++))
    else
        echo -e "${RED}✗${NC} $2 - NOT FOUND"
        ((FAILED++))
    fi
}

echo "1. System Checks"
echo "----------------------------------------"
check_command "python3" "Python 3 installed"
check_command "pip" "pip installed"

echo ""
echo "2. Python Version Check"
echo "----------------------------------------"
PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))' 2>/dev/null)
PYTHON_MINOR=$(python3 -c 'import sys; print(sys.version_info[1])' 2>/dev/null)

if [ -z "$PYTHON_VERSION" ]; then
    echo -e "${RED}✗${NC} Could not determine Python version"
    ((FAILED++))
else
    echo "Python version: $PYTHON_VERSION"
    if [ "$PYTHON_MINOR" -ge 8 ]; then
        echo -e "${GREEN}✓${NC} Python version is compatible (3.8+)"
        ((PASSED++))
    else
        echo -e "${RED}✗${NC} Python version too old (need 3.8+)"
        ((FAILED++))
    fi
fi

echo ""
echo "3. Virtual Environment Check"
echo "----------------------------------------"
if [ -n "$VIRTUAL_ENV" ]; then
    echo -e "${GREEN}✓${NC} Virtual environment is activated: $VIRTUAL_ENV"
    ((PASSED++))
else
    echo -e "${YELLOW}⚠${NC} Virtual environment NOT activated"
    echo "   Run: source venv/bin/activate"
    ((WARNINGS++))
fi

echo ""
echo "4. Required Python Packages"
echo "----------------------------------------"
check_package "pandas" "pandas"
check_package "numpy" "numpy"
check_package "openai" "openai"
check_package "mlflow" "mlflow"
check_package "jupyter" "jupyter"
check_package "requests" "requests"
check_package "python-dotenv" "dotenv"
check_package "jsonschema" "jsonschema"

echo ""
echo "5. Project Files"
echo "----------------------------------------"
check_file "llmops_assignment.ipynb" "Jupyter notebook"
check_file "requirements-rocky-linux.txt" "Requirements file (Linux)"
check_file ".env.example" ".env.example template"
check_file "src/config.py" "src/config.py module"
check_file "src/latency.py" "src/latency.py module"
check_file "src/cost.py" "src/cost.py module"
check_file "src/mlflow_manager.py" "src/mlflow_manager.py module"

echo ""
echo "6. Configuration Check"
echo "----------------------------------------"
if [ -f ".env" ]; then
    if grep -q "OPENAI_API_KEY" .env; then
        if grep -q "OPENAI_API_KEY=sk-" .env; then
            echo -e "${GREEN}✓${NC} .env file configured with API key"
            ((PASSED++))
        else
            echo -e "${YELLOW}⚠${NC} .env file exists but API key may not be valid"
            ((WARNINGS++))
        fi
    else
        echo -e "${RED}✗${NC} .env file missing OPENAI_API_KEY"
        ((FAILED++))
    fi
else
    echo -e "${RED}✗${NC} .env file NOT found"
    echo "   Run: cp .env.example .env"
    ((FAILED++))
fi

echo ""
echo "=========================================="
echo "Verification Summary"
echo "=========================================="
echo -e "${GREEN}Passed:${NC} $PASSED"
if [ "$FAILED" -gt 0 ]; then
    echo -e "${RED}Failed:${NC} $FAILED"
fi
if [ "$WARNINGS" -gt 0 ]; then
    echo -e "${YELLOW}Warnings:${NC} $WARNINGS"
fi

echo ""
if [ "$FAILED" -eq 0 ] && [ "$WARNINGS" -eq 0 ]; then
    echo -e "${GREEN}✓ All checks passed! Ready to run notebook.${NC}"
    echo ""
    echo "Next step:"
    echo "  jupyter notebook llmops_assignment.ipynb"
    exit 0
elif [ "$FAILED" -eq 0 ]; then
    echo -e "${YELLOW}⚠ Some warnings found, but you can proceed with caution.${NC}"
    echo ""
    echo "Review the warnings above and fix if needed, then run:"
    echo "  jupyter notebook llmops_assignment.ipynb"
    exit 0
else
    echo -e "${RED}✗ Some checks failed. Please fix the issues above.${NC}"
    exit 1
fi
