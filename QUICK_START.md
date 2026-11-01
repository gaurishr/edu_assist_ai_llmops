# Quick Start Guide - MLOps Assignment 2

This is a fast reference guide if you just want the commands without all the explanation.

## For macOS Users

If you've already set things up before, here's all you need:

```bash
# Activate your environment
source venv/bin/activate

# Verify everything's installed
python3 -c "import pandas, numpy, openai, mlflow; print('✓ All packages ready')"

# Run the notebook
jupyter notebook llmops_assignment.ipynb

# View MLflow results
mlflow ui --port 5000
```

## For Rocky Linux 9.5 Users (One-Time Setup)

First time setting up on Rocky Linux? Here's everything:

```bash
# Install system packages
sudo dnf install -y python3 python3-pip python3-venv gcc

# Go to the project directory
cd ~/Learnings/Assignments/MLOPS/edu_assist_ai_llmops

# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate

# Upgrade pip and related tools
pip install --upgrade pip setuptools wheel

# Install dependencies
pip install -r requirements-rocky-linux.txt

# Set up your configuration
cp .env.example .env
# Then edit with nano .env and add your OpenAI API key

# Verify it worked
python3 -c "import pandas, numpy, openai, mlflow; print('✓ All packages ready')"

# Run the notebook
jupyter notebook llmops_assignment.ipynb
```

## Rocky Linux Users (Every Time After That)

Once you've done the setup above, you just need this:

```bash
# Go to project
cd ~/Learnings/Assignments/MLOPS/edu_assist_ai_llmops

# Activate environment
source venv/bin/activate

# Run notebook
jupyter notebook llmops_assignment.ipynb
```

## Quick Verification Checklist

Before you run the notebook, make sure:

```bash
# Python is installed and new enough
python3 --version  # Should be 3.8 or higher

# You have a virtual environment set up
ls venv/bin/python3  # Should show your venv Python

# Your environment is activated
echo $VIRTUAL_ENV  # Should show your venv path

# All packages are there
pip list | grep -E "pandas|numpy|openai|mlflow"  # Should show all of them

# Your API key is configured
grep OPENAI_API_KEY .env  # Should show your key
```

## Running the Notebook

Once everything's ready:

```bash
jupyter notebook llmops_assignment.ipynb
```

Your browser will open automatically. The notebook has 20 cells total:
- Cells 1-7: Latency measurements
- Cells 8-11: Cost calculations
- Cells 12-18: MLflow experiments
- Cells 19-20: Summary and conclusions

Just run them in order from top to bottom.

## Viewing Your Results

After you run the notebook, you'll have output files. To see them formatted nicely with graphs and charts:

```bash
mlflow ui --port 5000
```

Then open your browser to `http://localhost:5000`

## Quick Troubleshooting

**Can't find pandas?**
Make sure you activated your environment first: `source venv/bin/activate`

**Port 8888 already in use?**
Use a different port: `jupyter notebook --port 8889 llmops_assignment.ipynb`

**API key not found?**
Edit your .env file and add your OpenAI key: `nano .env`

**Permission denied on scripts?**
Make them executable: `chmod +x setup.sh activate.sh verify_setup.sh`

## The Important Files

Here's what's in your project directory:

- `llmops_assignment.ipynb` - This is where you do the work
- `src/config.py` - Configuration settings
- `src/latency.py` - Code for measuring response times
- `src/cost.py` - Code for calculating costs
- `src/mlflow_manager.py` - Code for managing experiments
- `requirements.txt` - Package list for macOS
- `requirements-rocky-linux.txt` - Package list for Linux
- `.env.example` - Template for configuration
- `.env` - Your actual configuration (you create this)

## Helpful Documentation

- **START_HERE.md** - Full first-time setup guide
- **ROCKY_LINUX_SETUP.md** - Detailed Linux setup
- **README.md** - Complete reference documentation
- **DELIVERABLES.md** - What you need to submit
- **OPENAI_API_KEY_SETUP.md** - Getting your API key

## Next Step

Run this command:

For first time: `bash setup.sh`

For returning users: `bash activate.sh && jupyter notebook llmops_assignment.ipynb`

That's it!
