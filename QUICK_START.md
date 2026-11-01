# Quick Start Guide - MLOps Assignment 2

## For macOS Users (Already Set Up)

```bash
# Activate virtual environment
source venv/bin/activate

# Verify installation
python3 -c "import pandas, numpy, openai, mlflow; print('✓ All packages installed')"

# Run notebook
jupyter notebook llmops_assignment.ipynb
```

---

## For Rocky Linux 9.5 VM Users (New Setup)

### One-Time Setup (First Time Only)

```bash
# 1. Install system packages
sudo dnf install -y python3 python3-pip python3-venv gcc

# 2. Navigate to project
cd ~/Learnings/Assignments/MLOPS/edu_assist_ai_llmops

# 3. Create virtual environment
python3 -m venv venv

# 4. Activate it
source venv/bin/activate

# 5. Upgrade pip
pip install --upgrade pip setuptools wheel

# 6. Install dependencies
pip install -r requirements-rocky-linux.txt

# 7. Configure API key
cp .env.example .env
# Edit .env with your OpenAI API key
nano .env
```

### Every Time You Use the Project

```bash
# 1. Navigate to project
cd ~/Learnings/Assignments/MLOPS/edu_assist_ai_llmops

# 2. Activate virtual environment
source venv/bin/activate

# 3. Run notebook
jupyter notebook llmops_assignment.ipynb
```

---

## Verification Checklist

Before running the notebook, verify everything is set up correctly:

```bash
# Check Python version (should be 3.9+)
python3 --version

# Check virtual environment is activated (should show path with venv)
echo $VIRTUAL_ENV

# Check all packages are installed
python3 << 'EOF'
packages = ['pandas', 'numpy', 'openai', 'mlflow', 'jupyter']
for pkg in packages:
    try:
        __import__(pkg)
        print(f"✓ {pkg}")
    except ImportError:
        print(f"✗ {pkg} - NOT INSTALLED")
EOF

# Check API key is configured
grep -q "OPENAI_API_KEY" .env && echo "✓ API key configured" || echo "✗ API key NOT configured"
```

---

## Running the Notebook

Once verification passes:

```bash
# Start Jupyter
jupyter notebook llmops_assignment.ipynb

# Browser will open automatically, or open:
# http://localhost:8888

# Execute cells in order (1 → 20)
```

---

## Expected Outputs

After running the notebook, you'll see:

1. **latency_records.csv** - Latency measurements for each prompt version
2. **latency_stats.json** - Statistical summary
3. **cost_analysis.json** - Token counts and cost projections
4. **mlflow runs** - Experiment tracking data

View MLflow results:

```bash
mlflow ui --port 5000
# Open http://localhost:5000
```

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError: pandas` | Run: `source venv/bin/activate` |
| `pip: command not found` | Run: `sudo dnf install -y python3-pip` |
| `Port 8888 in use` | Run: `jupyter notebook --port 8889` |
| `OPENAI_API_KEY not found` | Edit `.env` and add your key |
| `Permission denied` errors | Don't use `sudo` with pip inside venv |

---

## Key Files

- **llmops_assignment.ipynb** - Main executable notebook (start here)
- **requirements-rocky-linux.txt** - All dependencies
- **.env.example** - API key template
- **ROCKY_LINUX_SETUP.md** - Detailed setup guide
- **src/** - Python modules (don't need to edit)

---

## Next Steps

1. ✓ Ensure system has Python 3.9+
2. ✓ Create and activate virtual environment
3. ✓ Install dependencies from requirements-rocky-linux.txt
4. ✓ Configure .env with OpenAI API key
5. ✓ Run `jupyter notebook llmops_assignment.ipynb`
6. ✓ Execute all 20 cells sequentially
7. ✓ View results in outputs/ and mlflow ui
