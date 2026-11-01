# MLOps Assignment 2: LLMOps - Deliverables Summary

**Course:** MLOps  
**Assignment:** Experiential Learning Assignment 2  
**Student:** Gauri Shanker (2025AF05069)  
**Date:** 2024-11-01  
**Repository:** edu_assist_ai_llmops  
**Location:** `/Users/gauri.shanker/Learnings/Assignments/MLOPS/edu_assist_ai_llmops`

---

## Executive Summary

This project implements a complete **LLMOps (Large Language Model Operations)** framework for operationalizing an academic question-answering assistant. The implementation covers three critical areas of LLM application management:

1. **API Latency Measurement** - Measuring and analyzing LLM API response times
2. **Token-based Cost Analysis** - Computing API costs and projected monthly expenses
3. **Prompt Versioning and MLflow Evaluation** - Managing and comparing prompt versions

**Total Marks:** 10 (5 for framework implementation, additional based on execution)

---

## Deliverables Checklist

### ✅ Core Implementation Files

| File | Status | Purpose |
|------|--------|---------|
| `src/config.py` | ✓ Complete | Configuration, constants, and model pricing |
| `src/latency.py` | ✓ Complete | Task 1: API calling and latency measurement |
| `src/cost.py` | ✓ Complete | Task 2: Token counting and cost calculation |
| `src/mlflow_manager.py` | ✓ Complete | Task 3: MLflow prompt versioning |
| `src/__init__.py` | ✓ Complete | Package initialization and exports |

### ✅ Notebooks and Scripts

| File | Status | Purpose |
|------|--------|---------|
| `llmops_assignment.ipynb` | ✓ Complete | Main Jupyter notebook with executable cells |
| `setup.sh` | ✓ Complete | Automated environment setup script |

### ✅ Configuration and Documentation

| File | Status | Purpose |
|------|--------|---------|
| `requirements.txt` | ✓ Complete | Python dependencies (30 packages) |
| `.env.example` | ✓ Complete | Environment variables template |
| `README.md` | ✓ Complete | Comprehensive setup and usage guide |
| `ASSIGNMENT_INSTRUCTIONS.md` | ✓ Complete | Full assignment specification |
| `.gitignore` | ✓ Updated | Version control configuration |

### ✅ Output Directories (Ready)

| Directory | Status | Purpose |
|-----------|--------|---------|
| `data/` | ✓ Created | Input data storage |
| `outputs/` | ✓ Created | Generated CSV output files |
| `screenshots/` | ✓ Created | MLflow screenshots directory |

---

## Task-by-Task Implementation

### Task 1: API Call and Latency Measurement (2 Marks)

**File:** `src/latency.py` + Notebook cells

**Classes Implemented:**
- `LatencyRecord`: Dataclass for storing latency metrics
- `LLMAPIClient`: API client with latency measurement
- `LatencyAnalyzer`: Statistical analysis of latency data

**Key Features:**
✓ Load API key from environment variable (no hardcoding)  
✓ Record: question ID, prompt version, model name, start/end time, latency, status  
✓ Calculate: mean, median, min, max, standard deviation  
✓ Error handling with graceful status tracking  
✓ Rate limiting (0.5s delays between requests)  
✓ Response text capture for analysis

**Deliverables Generated:**
- Latency table with 5 academic questions
- Statistical summary (mean, median, min, max, std dev)
- Slowest request analysis and interpretation
- CSV export: `latency_tokens_cost.csv`

**Sample Usage:**
```python
client = LLMAPIClient()
records = client.test_latency_for_all_questions("v1")
analyzer = LatencyAnalyzer()
stats = analyzer.analyze_records(records)
```

---

### Task 2: Token Counting and Cost Calculation (3 Marks)

**File:** `src/cost.py` + Notebook cells

**Classes Implemented:**
- `TokenUsage`: Dataclass for token counts
- `CostCalculation`: Dataclass for cost breakdown
- `TokenCounter`: Token extraction and estimation
- `CostCalculator`: Cost calculations with pricing formulas
- `CostOptimizationAnalyzer`: Actionable recommendations

**Pricing Formula Implementation:**
```
Input Cost = Input Tokens / 1,000,000 × Input Price per Million Tokens
Output Cost = Output Tokens / 1,000,000 × Output Price per Million Tokens
Total Cost per Request = Input Cost + Output Cost
Projected Monthly Cost = Average Cost per Request × 10,000
```

**Pricing Data (GPT-3.5-turbo):**
- Input: $0.50 per 1M tokens
- Output: $1.50 per 1M tokens

**Cost Optimization Recommendations:**
1. Reduce context size / prompt length
2. Shorten response lengths
3. Implement prompt caching
4. Optimize model selection
5. Batch process queries

**Deliverables Generated:**
- Token and cost table (input, output, total tokens, cost)
- Monthly projection for 10,000 requests
- Cost optimization recommendations
- Cost summary statistics

**Sample Usage:**
```python
cost_calc = CostCalculator.calculate_cost_for_tokens(100, 50, "gpt-3.5-turbo")
monthly = CostCalculator.project_monthly_cost(cost_calc.total_cost_per_request)
```

---

### Task 3: MLflow Prompt Versioning and Evaluation (5 Marks)

**File:** `src/mlflow_manager.py` + Notebook cells

**Classes Implemented:**
- `PromptRegistry`: Register and manage prompt versions
- `PromptEvaluator`: Evaluate prompts on test questions
- `MLflowExperimentTracker`: Log runs and metrics to MLflow
- `PromptComparator`: Compare versions and recommend best

**Three Prompt Versions:**

**v1 - Basic Prompt:**
```
Answer the following student question clearly.
Question: {{question}}
```

**v2 - Structured Prompt:**
```
You are an academic assistant.
Answer the following student question in a clear, concise, and accurate manner.
Use simple language suitable for undergraduate students.
Question: {{question}}
```

**v3 - JSON Output Prompt:**
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

**Logged Metrics per Version:**
- `avg_latency_seconds`: Average response time
- `avg_input_tokens`: Mean input token count
- `avg_output_tokens`: Mean output token count
- `avg_cost_per_request`: Mean cost per API call
- `valid_json`: JSON validity rate (v3 only)
- `projected_monthly_cost`: Scaled cost projection

**MLflow Integration:**
- Experiment: `eduassist_llmops_assignment`
- Runs logged for each prompt version
- Metrics aggregated from 5 test questions
- Artifacts: evaluation results, prompt info
- Production alias promotion supported

**Prompt Comparison Table:**
| Prompt Version | Avg Latency | Avg Input Tokens | Avg Output Tokens | Avg Cost | Valid JSON | Recommended |
|---|---|---|---|---|---|---|
| v1 | (measured) | (measured) | (measured) | (calculated) | N/A | Based on score |
| v2 | (measured) | (measured) | (measured) | (calculated) | N/A | Based on score |
| v3 | (measured) | (measured) | (measured) | (calculated) | (%) | Best if JSON valid |

**Deliverables Generated:**
- MLflow experiment with 3 runs
- Prompt Registry with v1, v2, v3
- Comparison table (CSV): `prompt_evaluation_results.csv`
- Best version selected and promoted
- Production alias assignment
- Promotion justification (150+ words minimum)

**Sample Usage:**
```python
registry = PromptRegistry()
registry.register_all_prompts()

evaluator = PromptEvaluator(api_client)
results = evaluator.evaluate_all_versions(PROMPTS)

tracker = MLflowExperimentTracker(registry)
run_ids = tracker.log_all_runs(evaluator)

comparator = PromptComparator()
comparison = comparator.compare_versions(evaluator)
```

---

## Test Data and Questions

Five academic questions for testing:

1. **Q1:** "What is photosynthesis and why is it important for life on Earth?"
2. **Q2:** "Explain the difference between mitosis and meiosis."
3. **Q3:** "What are the three main types of rocks and how are they formed?"
4. **Q4:** "Describe the water cycle and its importance in the environment."
5. **Q5:** "What is the significance of the Pythagorean theorem in mathematics?"

**Testing Coverage:** Each prompt version tested on all 5 questions = 15 total API calls

---

## Output Files Structure

### CSV Outputs
```
outputs/
├── latency_tokens_cost.csv          # Task 1 & 2 data
│   ├── Question ID
│   ├── Prompt Version
│   ├── Model Name
│   ├── Latency (seconds)
│   ├── Input/Output Tokens
│   └── Cost per Request
│
└── prompt_evaluation_results.csv    # Task 3 comparison
    ├── Prompt Version
    ├── Avg Latency
    ├── Avg Input Tokens
    ├── Avg Output Tokens
    ├── Avg Cost
    ├── Valid JSON Rate
    └── Recommended
```

### MLflow Artifacts
```
mlruns/
├── 0/                               # Experiment ID
│   ├── runs/
│   │   ├── run_v1_id/
│   │   │   ├── metrics/
│   │   │   ├── params/
│   │   │   └── artifacts/
│   │   ├── run_v2_id/
│   │   └── run_v3_id/
│   └── meta.yaml
```

---

## Project Dependencies

### Core Libraries
- **openai** (1.3.0) - OpenAI API client
- **mlflow** (2.10.0) - Experiment tracking and model registry
- **pandas** (2.1.0) - Data manipulation
- **numpy** (1.24.3) - Numerical computing
- **python-dotenv** (1.0.0) - Environment variable management

### Additional Tools
- **jupyter** (1.0.0) - Interactive notebook environment
- **requests** (2.31.0) - HTTP library
- **jsonschema** (4.19.0) - JSON validation
- **pydantic** (2.4.0) - Data validation

**Total:** 30 packages specified in `requirements.txt`

---

## Setup and Execution Instructions

### Quick Start
```bash
# 1. Navigate to project
cd /Users/gauri.shanker/Learnings/Assignments/MLOPS/edu_assist_ai_llmops

# 2. Activate environment
source venv/bin/activate

# 3. Configure API key
cp .env.example .env
# Edit .env and add OPENAI_API_KEY

# 4. Run notebook
jupyter notebook llmops_assignment.ipynb
```

### MLflow Tracking
```bash
# Start MLflow UI
mlflow ui --port 5000

# View at http://localhost:5000
```

### Expected Execution Time
- **Setup:** 5-10 minutes
- **API Calls:** 30-60 seconds (5 questions × 3 versions)
- **Cost Calculation:** < 1 second
- **MLflow Logging:** < 5 seconds
- **Total:** 3-4 hours including analysis

---

## Code Quality and Documentation

✓ **Comprehensive Docstrings:** All classes and methods documented  
✓ **Type Hints:** Full type annotations for function signatures  
✓ **Error Handling:** Try-except blocks with meaningful error messages  
✓ **Code Organization:** Modular structure with clear separation of concerns  
✓ **Environment Security:** API keys via .env, never hardcoded  
✓ **Comments:** Inline comments explaining complex logic  

---

## Academic Integrity Compliance

✓ **API Key Management:** Uses environment variables, not hardcoded  
✓ **Transparency:** Model name, API version, pricing date documented  
✓ **No Secrets:** .env excluded from version control  
✓ **Attribution:** Methods documented with sources and formulas  
✓ **Cost Control:** Reasonable API usage with rate limiting  

---

## Git Repository Status

**Repository:** edu_assist_ai_llmops  
**Location:** `/Users/gauri.shanker/Learnings/Assignments/MLOPS/edu_assist_ai_llmops`  
**Branch:** main  
**Commits:** 3

```
b31858c Add main Jupyter notebook and update gitignore
d25fffb Build complete MLOps Assignment 2: LLMOps framework
6c5e482 Initial commit: Add MLOps Assignment 2 specification
```

**Git Configuration:** Applied to Learnings directory only
- User: Gauri Shanker
- Email: 2025af05069@wilp.bits-pilani.ac.in

---

## Next Steps for Execution

### 1. Prepare Environment
```bash
cd /Users/gauri.shanker/Learnings/Assignments/MLOPS/edu_assist_ai_llmops
cp .env.example .env
# Add OPENAI_API_KEY to .env
```

### 2. Run Notebook
```bash
source venv/bin/activate
jupyter notebook llmops_assignment.ipynb
```

### 3. Execute Cells Sequentially
- Cell 1: Setup and imports
- Cells 2-4: Task 1 - Latency measurement
- Cells 5-7: Task 2 - Cost analysis
- Cells 8-12: Task 3 - MLflow evaluation
- Cell 13: Summary and conclusions

### 4. Review Outputs
- Check `outputs/` for CSV files
- View MLflow UI at http://localhost:5000
- Take screenshots as required

### 5. Generate Report
- Summarize findings in 500-700 words
- Export notebook to PDF
- Create submission ZIP file

---

## Submission Deliverables

The following must be submitted:

- ✓ `llmops_assignment.ipynb` - Executable notebook
- ✓ `requirements.txt` - All dependencies
- ✓ `outputs/latency_tokens_cost.csv` - Task 1 & 2 results
- ✓ `outputs/prompt_evaluation_results.csv` - Task 3 results
- ✓ MLflow screenshots (5-6 images):
  - Experiment overview with metrics
  - Prompt Registry showing v1, v2, v3
  - Prompt comparison or diff view
  - Production alias promotion
- ✓ PDF report (500-700 words)
- ✓ `README.md` - Setup and reproduction steps
- ✓ All files in a single ZIP: `edu_assist_ai_llmops_submission.zip`

---

## Marks Distribution

| Component | Marks | Status |
|-----------|-------|--------|
| Task 1: Latency Measurement | 2 | ✓ Framework Complete |
| Task 2: Cost Calculation | 3 | ✓ Framework Complete |
| Task 3: MLflow Evaluation | 5 | ✓ Framework Complete |
| **Total** | **10** | **✓ Ready for Execution** |

---

## References

### Documentation
- OpenAI API: https://platform.openai.com/docs
- MLflow Tracking: https://mlflow.org/docs/latest/tracking.html
- Python Environment: https://docs.python.org/3/tutorial/venv.html

### Assignment Resources
- Assignment PDF: `MLOps Assignment - 2.pdf`
- Assignment Instructions: `ASSIGNMENT_INSTRUCTIONS.md`
- Project README: `README.md`

---

## Support and Troubleshooting

For common issues, see README.md sections:
- Common Issues and Troubleshooting
- Performance Expectations
- Contact and Support

---

**Document Generated:** 2024-11-01  
**Project Status:** ✅ **READY FOR EXECUTION**  
**Framework Completion:** 100%

---

*All components are in place. The assignment is ready to be executed by running the Jupyter notebook with a valid OpenAI API key configured.*
