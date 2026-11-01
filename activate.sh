#!/bin/bash
################################################################################
# MLOps Assignment 2 - Integrated Activation Script
# This script activates the environment and provides quick commands
################################################################################

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
    echo "$1"
    echo -e "${BLUE}========================================${NC}"
    echo ""
}

# Check if venv exists
if [ ! -d "venv" ]; then
    echo -e "${RED}✗${NC} Virtual environment not found!"
    echo ""
    echo "Please run setup first:"
    echo -e "  ${BLUE}bash setup.sh${NC}"
    exit 1
fi

# Activate virtual environment
source venv/bin/activate

print_header "MLOps Assignment 2 - Environment Activated"

# Check if .env is configured
if [ ! -f ".env" ]; then
    echo -e "${YELLOW}⚠${NC} .env file not found. Run: cp .env.example .env"
    HAS_ENV=0
elif ! grep -q "OPENAI_API_KEY=sk-" .env; then
    echo -e "${YELLOW}⚠${NC} API key may not be configured in .env"
    HAS_ENV=0
else
    echo -e "${GREEN}✓${NC} Environment variables configured"
    HAS_ENV=1
fi

echo ""
echo "Python Environment:"
echo -e "  ${BLUE}Version:${NC} $(python3 --version 2>&1 | awk '{print $2}')"
echo -e "  ${BLUE}Location:${NC} $VIRTUAL_ENV"
echo ""

echo "Available Commands:"
echo ""
echo -e "  ${BLUE}Jupyter Notebook:${NC}"
echo "    jupyter notebook llmops_assignment.ipynb"
echo ""
echo -e "  ${BLUE}MLflow Tracking UI:${NC}"
echo "    mlflow ui --port 5000"
echo "    Then open: http://localhost:5000"
echo ""
echo -e "  ${BLUE}Verify Setup:${NC}"
echo "    bash verify_setup.sh"
echo ""
echo -e "  ${BLUE}Python REPL:${NC}"
echo "    python3"
echo ""
echo -e "  ${BLUE}List Installed Packages:${NC}"
echo "    pip list"
echo ""

# Additional helpful information
echo "Project Structure:"
echo "  ./src/                 - Python modules"
echo "  ./data/                - Test data"
echo "  ./outputs/             - Generated CSV files"
echo "  ./screenshots/         - MLflow screenshots"
echo "  ./llmops_assignment.ipynb - Main notebook"
echo ""

echo "Documentation:"
echo "  QUICK_START.md         - Fast setup guide"
echo "  ROCKY_LINUX_SETUP.md   - Detailed Linux setup"
echo "  README.md              - Complete documentation"
echo "  DELIVERABLES.md        - Expected outputs"
echo ""

if [ "$HAS_ENV" -eq 1 ]; then
    echo -e "${GREEN}Ready to start!${NC}"
    echo ""
    echo "Quick start:"
    echo -e "  ${BLUE}jupyter notebook llmops_assignment.ipynb${NC}"
else
    echo -e "${YELLOW}Please configure .env first:${NC}"
    echo -e "  ${BLUE}nano .env${NC}"
    echo ""
    echo "Then run:"
    echo -e "  ${BLUE}jupyter notebook llmops_assignment.ipynb${NC}"
fi

echo ""
