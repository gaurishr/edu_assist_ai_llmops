# 🚀 START HERE - MLOps Assignment 2

Welcome! This guide will help you get started with the LLMOps assignment quickly.

---

## For First-Time Users: Complete Setup

### Step 1: Run Setup Script

```bash
bash setup.sh
```

This script will:

- ✓ Detect your operating system (macOS or Rocky Linux)
- ✓ Create a Python virtual environment
- ✓ Install all dependencies automatically
- ✓ Create necessary directories
- ✓ Set up your .env configuration file

### Step 2: Configure API Key

```bash
# Edit .env and add your OpenAI API key
nano .env
```

Add your key like this:

```
OPENAI_API_KEY=sk-your-actual-key-here
```

[Need help getting an API key?](OPENAI_API_KEY_SETUP.md)

### Step 3: Verify Setup

```bash
bash verify_setup.sh
```

This checks:

- ✓ All required packages installed
- ✓ Python version compatible
- ✓ .env file properly configured
- ✓ All project files present

### Step 4: Run the Notebook

```bash
bash activate.sh
jupyter notebook llmops_assignment.ipynb
```

---

## For Returning Users: Quick Start

```bash
# 1. Activate environment
bash activate.sh

# 2. Run notebook
jupyter notebook llmops_assignment.ipynb

# 3. (Optional) View MLflow results
mlflow ui --port 5000
```

---

## Integration of Setup & Activate Scripts

The **setup.sh** and **activate.sh** scripts work together:

```
setup.sh (one time)
    ↓
    └─→ Creates venv
    └─→ Installs dependencies
    └─→ Sets up .env
    └─→ Creates directories

    ↓
  
activate.sh (every session)
    └─→ Activates virtual environment
    └─→ Shows available commands
    └─→ Checks .env configuration
```

### Smart Platform Detection

- **Linux/Rocky**: Uses `requirements-rocky-linux.txt`
- **macOS**: Uses `requirements.txt`

---

## Key Features

### 📊 Three Integrated Tasks

1. **Latency Measurement** - Measure API response times
2. **Cost Analysis** - Calculate token usage and costs
3. **MLflow Tracking** - Manage and compare prompt versions

### 🛠️ Automated Scripts

- **setup.sh** - One-time environment setup
- **activate.sh** - Activate environment with helpful tips
- **verify_setup.sh** - Check installation is correct

### 📚 Comprehensive Docs

- **QUICK_START.md** - Fast reference guide
- **ROCKY_LINUX_SETUP.md** - Detailed Linux setup
- **README.md** - Full documentation
- **DELIVERABLES.md** - Expected outputs

---

## File Structure

```
edu_assist_ai_llmops/
├── setup.sh                         ← Run first (one time)
├── activate.sh                      ← Run each session
├── verify_setup.sh                  ← Check setup status
│
├── START_HERE.md                    ← You are here
├── QUICK_START.md                   ← Quick reference
├── ROCKY_LINUX_SETUP.md             ← Linux detailed guide
├── OPENAI_API_KEY_SETUP.md          ← API key help
├── README.md                        ← Full docs
├── DELIVERABLES.md                  ← Expected outputs
│
├── llmops_assignment.ipynb          ← Main notebook (run this!)
├── requirements.txt                 ← Dependencies (macOS)
├── requirements-rocky-linux.txt     ← Dependencies (Linux)
├── .env.example                     ← Configuration template
├── .env                             ← Your config (after setup)
│
├── src/                             ← Python modules
│   ├── config.py                    ← Configuration hub
│   ├── latency.py                   ← Task 1: Latency
│   ├── cost.py                      ← Task 2: Cost
│   └── mlflow_manager.py            ← Task 3: MLflow
│
├── data/                            ← Test questions
├── outputs/                         ← Generated CSV files
├── screenshots/                     ← MLflow screenshots
└── mlruns/                          ← MLflow experiment data
```

---

## Typical Workflow

### First Time

```bash
# 1. Clone/download project
cd ~/Learnings/Assignments/MLOPS/edu_assist_ai_llmops

# 2. Run integrated setup (creates venv, installs deps)
bash setup.sh

# 3. Configure API key
nano .env

# 4. Verify everything works
bash verify_setup.sh

# 5. Activate and run
bash activate.sh
jupyter notebook llmops_assignment.ipynb
```

### Subsequent Times

```bash
# Just activate and run
bash activate.sh
jupyter notebook llmops_assignment.ipynb
```

---

## Jupyter Notebook Overview

The notebook has 20 cells covering 3 tasks:

| Cells | Task              | Description                                      |
| ----- | ----------------- | ------------------------------------------------ |
| 1-7   | **Latency** | Measure API response times for 3 prompt versions |
| 8-11  | **Cost**    | Calculate tokens and project monthly costs       |
| 12-18 | **MLflow**  | Track experiments and compare versions           |
| 19-20 | **Summary** | Results and conclusions                          |

**Run cells sequentially (1 → 20)**

---

## Expected Outputs

After running the notebook:

| File                                      | Description                     |
| ----------------------------------------- | ------------------------------- |
| `outputs/latency_tokens_cost.csv`       | Raw measurements                |
| `outputs/prompt_evaluation_results.csv` | MLflow evaluation results       |
| `mlruns/`                               | MLflow experiment tracking data |

View MLflow results:

```bash
mlflow ui --port 5000
# Open: http://localhost:5000
```

---

## Common Issues & Solutions

| Issue                            | Solution                              |
| -------------------------------- | ------------------------------------- |
| `ModuleNotFoundError: pandas`  | Run: `bash activate.sh`             |
| `venv not found`               | Run: `bash setup.sh`                |
| `OPENAI_API_KEY not found`     | Edit `.env` with your key           |
| `Port 8888 in use`             | Run: `jupyter notebook --port 8889` |
| `Permission denied` on scripts | Run: `chmod +x *.sh`                |

---

## Platform-Specific Notes

### macOS

- Uses `requirements.txt` (pre-built wheels, faster)
- Python 3.14 available through Homebrew
- Virtual environment is platform-specific

### Rocky Linux 9.5

- Uses `requirements-rocky-linux.txt` (compatible versions)
- Requires system packages: `sudo dnf install -y python3 python3-pip python3-venv gcc`
- See [ROCKY_LINUX_SETUP.md](ROCKY_LINUX_SETUP.md) for details

---

## Getting Help

1. **Quick questions?** → [QUICK_START.md](QUICK_START.md)
2. **Linux setup help?** → [ROCKY_LINUX_SETUP.md](ROCKY_LINUX_SETUP.md)
3. **API key issues?** → [OPENAI_API_KEY_SETUP.md](OPENAI_API_KEY_SETUP.md)
4. **Full documentation?** → [README.md](README.md)
5. **What to deliver?** → [DELIVERABLES.md](DELIVERABLES.md)

---

## Quick Command Reference

```bash
# Setup (one time)
bash setup.sh

# Activate (every session)
bash activate.sh

# Verify installation
bash verify_setup.sh

# Run notebook
jupyter notebook llmops_assignment.ipynb

# View MLflow
mlflow ui --port 5000

# Check installed packages
pip list

# Deactivate virtual environment
deactivate
```

---

## Next Steps

✅ **1. Run setup:** `bash setup.sh`
✅ **2. Configure API:** Edit `.env`
✅ **3. Verify setup:** `bash verify_setup.sh`
✅ **4. Start notebook:** `bash activate.sh && jupyter notebook llmops_assignment.ipynb`
