#!/bin/bash
# Setup script for MLOps Assignment 2

echo "=== Setting up EDU Assist AI - LLMOps Assignment ==="

# Create virtual environment if not exists
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install --upgrade pip -q
pip install -r requirements.txt -q

echo "✓ Setup complete!"
echo "To activate environment, run: source venv/bin/activate"
