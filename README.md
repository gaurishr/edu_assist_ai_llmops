# EDU Assist AI - LLMOps Assignment 2

## Overview

This project implements a complete LLMOps (Large Language Model Operations) solution for operationalizing an academic question-answering assistant. The assignment covers three key aspects of LLM application management:

1. **API Latency Measurement** - Measuring response times for LLM API calls
2. **Token-based Cost Analysis** - Calculating API costs based on token usage
3. **Prompt Versioning and MLflow Evaluation** - Managing and comparing prompt versions in MLflow

## Learning Outcomes

After completing this assignment, you will be able to:

- Explain LLMOps and its differences from traditional MLOps
- Call an LLM through an API and measure response latency
- Extract token usage information and compute request-level and projected monthly costs
- Register, compare, evaluate, and promote prompt versions in MLflow
- Create JSON-output prompts and validate them using a valid_json metric

## Project Structure

```
edu_assist_ai_llmops/
├── llmops_assignment.ipynb      # Main Jupyter notebook with all tasks
├── requirements.txt              # Python dependencies
├── setup.sh                       # Setup script
├── README.md                      # This file
├── .env.example                   # Environment variables template
├── ASSIGNMENT_INSTRUCTIONS.md    # Full assignment specification
├── src/                          # Python source modules
│   ├── __init__.py              # Package initialization
│   ├── config.py                # Configuration and constants
│   ├── latency.py               # Task 1: Latency measurement
│   ├── cost.py                  # Task 2: Cost calculation
│   └── mlflow_manager.py        # Task 3: MLflow management
├── data/                        # Input data directory
├── outputs/                     # Generated outputs
│   ├── latency_tokens_cost.csv
│   └── prompt_evaluation_results.csv
└── screenshots/                 # MLflow screenshots directory
```

## Prerequisites

- **Python:** 3.8 or later (tested with Python 3.11)
- **OpenAI API Key:** Required for accessing GPT models
- **MLflow:** For prompt versioning and experiment tracking
- **Jupyter Notebook:** For running the interactive notebook

## Setup Instructions

### 1. Environment Setup

```bash
# Navigate to the project directory
cd /Users/gauri.shanker/Learnings/Assignments/MLOPS/edu_assist_ai_llmops

# Create and activate virtual environment (if not already done)
python3 -m venv venv
source venv/bin/activate

# Or use the setup script
bash setup.sh
```

### 2. Install Dependencies

```bash
# With virtual environment activated
pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Configure Environment Variables

```bash
# Create .env file from template
cp .env.example .env

# Edit .env and add your OpenAI API key
# OPENAI_API_KEY=sk-your-api-key-here
```

**Important:** 
- Never commit `.env` with real API keys to version control
- Keep API keys secure and use environment variables only
- API key should have access to GPT-3.5-turbo or GPT-4 models

### 4. Verify Setup

```bash
# Test imports
python3 -c "from src import LLMAPIClient, PromptRegistry; print('✓ Setup successful')"
```

## Running the Assignment

### Option 1: Jupyter Notebook (Recommended)

```bash
# Activate virtual environment
source venv/bin/activate

# Start Jupyter
jupyter notebook

# Open llmops_assignment.ipynb in the browser
# Run cells sequentially
```

### Option 2: Command Line

```bash
# Activate virtual environment
source venv/bin/activate

# Run the notebook as Python script
jupyter nbconvert --to script llmops_assignment.ipynb
python3 llmops_assignment.py
```

### MLflow Experiment Tracking

After running the assignment:

```bash
# Start MLflow UI
mlflow ui --port 5000

# Navigate to http://localhost:5000 in browser
# View experiments, metrics, and artifacts
```

## Tasks Breakdown

### Task 1: API Call and Latency Measurement (2 Marks)

**Objective:** Measure latency for LLM API calls on five academic questions.

**Deliverables:**
- ✓ Executable API-call code with proper error handling
- ✓ Latency table with question ID, prompt version, model, timestamps, and status
- ✓ Latency statistics (mean, median, min, max, std dev)
- ✓ Interpretation of slowest request and possible reasons

**Key Metrics:**
- Mean latency
- Median latency
- Min/Max latency range
- Standard deviation
- Response status codes

### Task 2: Token Counting and Cost Calculation (3 Marks)

**Objective:** Extract token usage and calculate costs based on OpenAI pricing.

**Deliverables:**
- ✓ Table with input tokens, output tokens, total tokens, and cost per request
- ✓ Monthly cost projection for 10,000 requests
- ✓ Cost optimization recommendations

**Formulas Used:**
```
Input Cost = Input Tokens / 1,000,000 × Input Price per Million Tokens
Output Cost = Output Tokens / 1,000,000 × Output Price per Million Tokens
Total Cost per Request = Input Cost + Output Cost
Projected Monthly Cost = Average Cost per Request × 10,000
```

**Pricing Reference (as of 2024):**
- gpt-3.5-turbo: $0.50/1M input tokens, $1.50/1M output tokens

### Task 3: MLflow Prompt Versioning and Evaluation (5 Marks)

**Objective:** Register, evaluate, and promote prompt versions in MLflow.

**Three Prompt Versions:**

**v1 - Basic:**
```
Answer the following student question clearly.
Question: {{question}}
```

**v2 - Structured:**
```
You are an academic assistant.
Answer the following student question in a clear, concise, and accurate manner.
Use simple language suitable for undergraduate students.
Question: {{question}}
```

**v3 - JSON Output:**
```
You are an academic assistant.
Answer the student question and return ONLY valid JSON.
Do not include markdown, explanations outside JSON, or code fences.

Use this exact JSON schema:
{
  "answer": "string",
  "confidence": "high | medium | low",
  "key_points": ["string"]
}
Question: {{question}}
```

**Logged Metrics:**
- `avg_latency_seconds`: Average response latency
- `avg_input_tokens`: Average input token count
- `avg_output_tokens`: Average output token count
- `avg_cost_per_request`: Average cost per API request
- `valid_json`: JSON validity rate (v3 only)

**Deliverables:**
- ✓ MLflow experiment screenshot showing runs and metrics
- ✓ Prompt Registry screenshot showing v1, v2, v3
- ✓ Prompt comparison table with all metrics
- ✓ Production alias promotion screenshot
- ✓ Promotion justification (150+ words)

## Test Questions

The assignment uses five academic questions:

1. "What is photosynthesis and why is it important for life on Earth?"
2. "Explain the difference between mitosis and meiosis."
3. "What are the three main types of rocks and how are they formed?"
4. "Describe the water cycle and its importance in the environment."
5. "What is the significance of the Pythagorean theorem in mathematics?"

## Output Files

The assignment generates the following output files:

### CSV Files
- **latency_tokens_cost.csv**: Latency and cost data for all requests
- **prompt_evaluation_results.csv**: Comparison of all prompt versions

### MLflow Artifacts
- Experiment runs with metrics and parameters
- Prompt versions with commit messages
- Evaluation results stored as artifacts

## Evaluation Criteria

| Component | Marks | Criteria |
|-----------|-------|----------|
| Task 1: Latency | 2 | API calls working, latency measured accurately, statistics calculated |
| Task 2: Cost | 3 | Token counting correct, cost calculations accurate, monthly projection included |
| Task 3: MLflow | 5 | All 3 prompts registered, metrics logged, best version promoted, justification provided |
| **Total** | **10** | Complete implementation with all deliverables |

## Academic Integrity Guidelines

✓ **Do:**
- Use environment variables for API keys (never hardcode)
- Mention model name, API version, pricing date, and currency
- Document the tool/method used for token counting
- Keep API costs reasonable during testing

✗ **Don't:**
- Expose API keys, billing information, or personal data
- Commit sensitive credentials to version control
- Copy code without attribution

## Common Issues and Troubleshooting

### Issue: `OPENAI_API_KEY not set`
**Solution:** 
- Create `.env` file with `OPENAI_API_KEY=your-key`
- Ensure `.env` is in the project root directory
- Run `source venv/bin/activate` and verify environment

### Issue: `Module not found: src`
**Solution:**
- Ensure you're running from project root directory
- Virtual environment is activated
- `sys.path.insert(0, './src')` is at the beginning of the notebook

### Issue: `MLflow experiment not found`
**Solution:**
- Start MLflow UI: `mlflow ui --port 5000`
- Ensure MLflow is installed: `pip install mlflow`
- Check `MLFLOW_TRACKING_URI` in .env is correct

### Issue: API rate limiting or timeout
**Solution:**
- Implemented delays between API calls (0.5s)
- Consider using gpt-3.5-turbo (faster than gpt-4)
- Reduce `max_tokens` parameter if needed

## Performance Expectations

- **Latency:** 2-10 seconds per request (varies by model and network)
- **Total Execution Time:** 3-4 hours (as per assignment specification)
- **Cost Estimation:** $0.05-0.20 for all 15 API calls (5 questions × 3 versions)

## Resources

### Documentation
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [MLflow Tracking Documentation](https://mlflow.org/docs/latest/tracking.html)
- [MLflow Prompt Registry](https://mlflow.org/docs/latest/llm-evaluate/)
- [OpenAI Pricing](https://openai.com/pricing)

### Related Concepts
- **LLMOps vs MLOps:** Differences in managing LLM applications
- **Token Economics:** Understanding token-based billing
- **Prompt Engineering:** Optimizing prompts for quality and cost
- **Experiment Tracking:** Using MLflow for reproducibility

## Author Information

- **Name:** Gauri Shanker
- **ID:** 2025AF05069
- **Course:** MLOps
- **Assignment:** Experiential Learning Assignment 2
- **Date:** 2024

## Submission Checklist

Before submitting, ensure you have:

- [ ] Jupyter notebook with executable code
- [ ] requirements.txt with all dependencies
- [ ] latency_tokens_cost.csv output file
- [ ] prompt_evaluation_results.csv output file
- [ ] MLflow screenshots (experiment, prompts, metrics, promotion)
- [ ] Report in PDF format (500-700 words)
- [ ] README with setup and reproduction steps
- [ ] All code commented and documented
- [ ] No API keys or secrets in version control

## Git Workflow

```bash
# View status
git status

# Add changes
git add .

# Commit with meaningful message
git commit -m "Task 1: Latency measurement complete"

# View history
git log --oneline
```

## Contact and Support

For questions about the assignment, refer to:
- Assignment PDF: MLOps Assignment - 2.pdf
- MLflow Documentation: https://mlflow.org
- OpenAI Support: https://help.openai.com

---

**Last Updated:** 2024-11-01  
**Status:** Ready for Execution

## Author
Gauri Shanker (2025AF05069)
