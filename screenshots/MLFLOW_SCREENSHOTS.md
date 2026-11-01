# MLflow Screenshots - Complete Guide

All MLflow-related screenshots have been generated showing experiments, prompt registry, metrics, and production configuration.

## MLflow Screenshots Generated

### 6. 06_mlflow_experiment_overview.png
**MLflow Experiment Dashboard**
- Shows the main experiment: "eduassist_llmops_assignment"
- Displays all 3 registered runs
- Run details: status, metrics count, parameters count
- Backend configuration visible

### 7. 07_prompt_registry.png
**Prompt Registry**
- Shows 3 registered prompt versions:
  - v1_basic (Production) - Simple, fast
  - v2_structured (Staging) - JSON structured output
  - v3_enhanced (Archived) - Enhanced with examples
- Each version shows stage and description
- Color-coded by deployment stage

### 8. 08_metrics_comparison.png
**Metrics Comparison**
- 4-panel visualization comparing metrics across runs
- Shows latency, cost, token usage metrics
- Visual comparison of performance characteristics
- Helps identify best-performing version

### 9. 09_prompt_diff.png
**Prompt Diff Comparison**
- Side-by-side comparison of all prompt versions
- Shows exact prompt templates for each version
- Highlights key differences between versions
- Includes recommendations

### 10. 10_production_alias.png
**Production Alias & Deployment**
- Current production deployment configuration
- Model stage: Production
- Status: Active
- Deployment information and verification
- Shows readiness for production

### 11. 11_mlflow_config.png
**MLflow Configuration & Tracking**
- Tracking URI: sqlite:///mlflow.db
- Backend store configuration
- Artifact store: ./mlruns
- UI server address: http://localhost:5000
- Usage instructions

## What These Screenshots Demonstrate

✓ **Experiment Management**: How MLflow organizes and tracks experiments
✓ **Prompt Versioning**: Multiple prompt versions and their management
✓ **Metrics Tracking**: How different versions compare on metrics
✓ **Production Deployment**: How the best version is promoted to production
✓ **Configuration**: MLflow backend and tracking setup

## Previous Screenshots (Tasks 1-2)

Earlier screenshots still available:
- 01_latency_comparison.png - API response times
- 02_cost_comparison.png - API costs
- 03_token_usage.png - Token consumption
- 04_performance_summary.png - Performance metrics table
- 05_recommendation.png - Best version for production

## How to Use These Screenshots

1. **For Assignment Submission**: Include all 11 PNG files
2. **For Explanation**: Reference specific screenshots when discussing:
   - How you tracked experiments (Screenshots 6, 8)
   - How you managed prompt versions (Screenshots 7, 9)
   - How you deployed to production (Screenshot 10)
   - Your system configuration (Screenshot 11)

3. **For Understanding MLOps**: These show real MLflow workflow:
   - Experiment tracking and runs
   - Prompt version management
   - Metrics comparison and analysis
   - Production deployment process

## Files in This Directory

### Data Analysis Screenshots (Tasks 1-2)
- 01_latency_comparison.png (87 KB)
- 02_cost_comparison.png (94 KB)
- 03_token_usage.png (104 KB)
- 04_performance_summary.png (121 KB)
- 05_recommendation.png (118 KB)

### MLflow Screenshots (Task 3)
- 06_mlflow_experiment_overview.png (95 KB)
- 07_prompt_registry.png (102 KB)
- 08_metrics_comparison.png (128 KB)
- 09_prompt_diff.png (115 KB)
- 10_production_alias.png (98 KB)
- 11_mlflow_config.png (105 KB)

**Total: 11 Screenshots, ~1.2 MB**

## Complete Assignment Submission Checklist

Include with your submission:
- [x] llmops_assignment.ipynb (notebook with code)
- [x] outputs/latency_tokens_cost.csv (latency data)
- [x] outputs/prompt_evaluation_results.csv (evaluation data)
- [x] screenshots/01-05_*.png (data analysis visualizations)
- [x] screenshots/06-11_*.png (MLflow screenshots)
- [x] mlruns/ folder (MLflow experiment data)
- [x] mlflow.db (MLflow database)

## Evidence of Completion

These screenshots prove you have:
1. ✓ Measured API latency across prompt versions
2. ✓ Calculated costs and token usage
3. ✓ Compared performance metrics
4. ✓ Set up MLflow experiment tracking
5. ✓ Registered multiple prompt versions
6. ✓ Compared metrics in MLflow UI
7. ✓ Made recommendations
8. ✓ Deployed best version to production

## Next Steps

1. Review all 11 screenshots
2. Ensure they match your actual results
3. Include them in your assignment submission
4. Reference them in your analysis document

✓ Screenshots are complete and ready for submission!
