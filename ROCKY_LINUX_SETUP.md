# Setting Up on Rocky Linux 9.5

If you're working on a Rocky Linux 9.5 virtual machine, here's the detailed guide to get everything working.

## Quick Setup (Copy and Paste)

If you just want to get going, here are the commands you can copy and paste into your terminal:

```bash
# Update system and install Python
sudo dnf update -y
sudo dnf install -y python3 python3-pip python3-venv gcc

# Go to your project
cd ~/Learnings/Assignments/MLOPS/edu_assist_ai_llmops

# Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# Upgrade the package installer
pip install --upgrade pip setuptools wheel

# Install all the dependencies
pip install -r requirements-rocky-linux.txt

# Set up your configuration
cp .env.example .env
nano .env  # Add your OpenAI API key here

# Verify everything works
python3 -c "import pandas, numpy, openai, mlflow; print('✓ Ready to go!')"

# Run the notebook
jupyter notebook llmops_assignment.ipynb
```

## Detailed Walkthrough

### Step 1: Install System Packages

Rocky Linux comes pretty minimal, so we need to install Python first:

```bash
sudo dnf install -y python3 python3-pip python3-venv gcc
```

This installs Python 3, the pip package manager, the venv module for virtual environments, and gcc for compiling code if needed. The `-y` flag means "yes to everything" so you don't have to confirm.

Verify it worked:

```bash
python3 --version  # Should show 3.9.x or higher
```

### Step 2: Navigate to Your Project

```bash
cd ~/Learnings/Assignments/MLOPS/edu_assist_ai_llmops
```

Make sure you're in the right directory. You should see the `src` folder and Python files here.

### Step 3: Create a Virtual Environment

A virtual environment is a separate Python installation just for this project. It keeps everything isolated:

```bash
python3 -m venv venv
source venv/bin/activate
```

You should now see `(venv)` at the beginning of your command prompt. That means you're inside the virtual environment.

### Step 4: Upgrade pip and Tools

Python comes with pip, but we want to make sure we have the newest version:

```bash
pip install --upgrade pip setuptools wheel
```

This usually takes just a minute.

### Step 5: Install All the Dependencies

All the Python packages you need are listed in requirements-rocky-linux.txt. Install them all at once:

```bash
pip install -r requirements-rocky-linux.txt
```

This might take a few minutes as it downloads and installs 30+ packages. You'll see output as it goes.

### Step 6: Set Up Your Configuration

We need to tell the system your OpenAI API key:

```bash
cp .env.example .env
nano .env
```

Find the line that says `OPENAI_API_KEY=` and add your actual key. It should look like:

```
OPENAI_API_KEY=sk-your-actual-key-here
```

Press Ctrl+X, then Y, then Enter to save.

### Step 7: Verify Everything Works

Let's make sure all the packages installed correctly:

```bash
python3 << 'VERIFY'
import pandas as pd
import numpy as np
import openai
import mlflow
print("✓ All packages installed successfully!")
print(f"  pandas: {pd.__version__}")
print(f"  numpy: {np.__version__}")
VERIFY
```

If you see the success message, you're good to go.

### Step 8: Run the Notebook

Now you're ready to run the actual assignment:

```bash
jupyter notebook llmops_assignment.ipynb
```

The notebook should open in your browser (usually at http://localhost:8888). If it doesn't open automatically, look at the terminal output - it will give you a URL to paste into your browser.

## Every Time You Come Back

You don't need to do all the installation again. Just do this:

```bash
cd ~/Learnings/Assignments/MLOPS/edu_assist_ai_llmops
source venv/bin/activate
jupyter notebook llmops_assignment.ipynb
```

## Troubleshooting

**Python 3 not found**
Run: `sudo dnf install -y python3`

**pip command not found**
Run: `sudo dnf install -y python3-pip`

**venv module not found**
Run: `sudo dnf install -y python3-venv`

**Compilation errors during package install**
You're probably missing development tools. Run: `sudo dnf install -y gcc python3-devel`

**SSL certificate errors when downloading packages**
Try: `pip install --trusted-host pypi.python.org -r requirements-rocky-linux.txt`

**Port 8888 already in use**
Use a different port: `jupyter notebook --port 8889 llmops_assignment.ipynb`

**Can't activate venv**
Make sure you're in the right directory and the venv folder exists: `ls -la venv/`

## Verification Commands

Use these to check everything is set up correctly:

```bash
# Check Python version
python3 --version

# Check virtual environment is active (should show path)
echo $VIRTUAL_ENV

# Check installed packages
pip list | grep -E "pandas|numpy|openai|mlflow"

# Check API key is set
grep OPENAI_API_KEY .env
```

## Important Notes for Rocky Linux

- Rocky Linux 9.5 comes with Python 3.9, which is perfect for this project
- The `dnf` package manager is what you use instead of `apt` on Ubuntu
- Virtual environments are created locally in each project, not installed system-wide
- Don't use `sudo` when running `pip install` inside a venv - it's not needed and can cause problems

## Need More Help?

Check out these other guides:
- **START_HERE.md** - General getting started guide
- **QUICK_START.md** - Fast command reference
- **README.md** - Complete documentation
- **OPENAI_API_KEY_SETUP.md** - Help with API keys

You've got this!
