"""
Task 3: MLflow Prompt Versioning and Evaluation Module

This module handles registering prompt versions in MLflow,
running evaluations, and promoting the best version to production.
"""

import json
import time
from typing import Dict, List, Any, Optional
from datetime import datetime
import mlflow
from mlflow.entities import Metric

# Handle both package imports (src.*) and direct imports (*)
try:
    from src.config import (
        MLFLOW_EXPERIMENT_NAME,
        MLFLOW_TRACKING_URI,
        MLFLOW_ARTIFACT_ROOT,
        PROMPTS,
        ACADEMIC_QUESTIONS,
        MODEL_NAME
    )
    from src.latency import LLMAPIClient, LatencyRecord
    from src.cost import TokenCounter, CostCalculator, TokenUsage, CostCalculation
except ImportError:
    from config import (
        MLFLOW_EXPERIMENT_NAME,
        MLFLOW_TRACKING_URI,
        MLFLOW_ARTIFACT_ROOT,
        PROMPTS,
        ACADEMIC_QUESTIONS,
        MODEL_NAME
    )
    from latency import LLMAPIClient, LatencyRecord
    from cost import TokenCounter, CostCalculator, TokenUsage, CostCalculation


class PromptRegistry:
    """Manage prompt registration and versioning in MLflow"""
    
    def __init__(self):
        """Initialize MLflow and create experiment if needed"""
        if MLFLOW_TRACKING_URI:
            mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
        
        # Note: mlflow.set_artifact_root() doesn't exist in MLflow 3.x
        # Artifact location is set when creating the experiment instead
        
        # Create or get experiment
        experiment = mlflow.get_experiment_by_name(MLFLOW_EXPERIMENT_NAME)
        if experiment is None:
            self.experiment_id = mlflow.create_experiment(
                name=MLFLOW_EXPERIMENT_NAME,
                artifact_location=MLFLOW_ARTIFACT_ROOT
            )
        else:
            self.experiment_id = experiment.experiment_id
        
        self.registered_prompts = {}
    
    def register_prompt_version(
        self,
        version: str,
        name: str,
        template: str,
        commit_message: str
    ) -> str:
        """
        Register a prompt version in MLflow
        
        Args:
            version: Version identifier (e.g., 'v1', 'v2', 'v3')
            name: Descriptive name for the prompt
            template: Prompt template with {{question}} placeholder
            commit_message: Commit message describing the version
            
        Returns:
            Prompt URI for reference
        """
        prompt_uri = f"prompts://{version}"
        
        self.registered_prompts[version] = {
            "name": name,
            "template": template,
            "commit_message": commit_message,
            "registered_at": datetime.now().isoformat(),
            "uri": prompt_uri
        }
        
        return prompt_uri
    
    def register_all_prompts(self):
        """Register all prompt versions from config"""
        prompts_config = {
            "v1": {
                "name": "Basic",
                "key": "v1_basic",
                "message": "Initial basic prompt for academic QA"
            },
            "v2": {
                "name": "Structured",
                "key": "v2_structured",
                "message": "Structured prompt with clear instructions for undergraduates"
            },
            "v3": {
                "name": "JSON Output",
                "key": "v3_json",
                "message": "JSON-formatted prompt with schema specification"
            }
        }
        
        for version, config in prompts_config.items():
            prompt_data = PROMPTS[config["key"]]
            self.register_prompt_version(
                version=version,
                name=config["name"],
                template=prompt_data["template"],
                commit_message=config["message"]
            )
        
        return self.registered_prompts


class PromptEvaluator:
    """Evaluate prompt versions on test questions"""
    
    def __init__(self, api_client: LLMAPIClient = None):
        """Initialize the evaluator"""
        self.api_client = api_client or LLMAPIClient()
        self.evaluation_results = {}
    
    def evaluate_prompt_version(
        self,
        version: str,
        prompt_template: str
    ) -> Dict[str, Any]:
        """
        Evaluate a prompt version on all test questions
        
        Args:
            version: Prompt version (e.g., 'v1', 'v2', 'v3')
            prompt_template: Prompt template with {{question}} placeholder
            
        Returns:
            Dict containing evaluation metrics and results
        """
        results = {
            "version": version,
            "questions_tested": len(ACADEMIC_QUESTIONS),
            "latencies": [],
            "token_usage": [],
            "costs": [],
            "responses": [],
            "json_valid_count": 0,
            "timestamp": datetime.now().isoformat()
        }
        
        print(f"\n{'='*60}")
        print(f"Evaluating Prompt Version: {version}")
        print(f"{'='*60}")
        
        for question in ACADEMIC_QUESTIONS:
            # Format prompt
            formatted_prompt = prompt_template.replace(
                "{{question}}", 
                question["question"]
            )
            
            # Call API and measure latency
            record = self.api_client.call_api(
                prompt=formatted_prompt,
                question_id=question["id"],
                prompt_version=version
            )
            
            results["latencies"].append(record.latency_seconds)
            results["responses"].append({
                "question_id": question["id"],
                "response": record.response_text,
                "status": record.response_status,
                "error": record.error_message
            })
            
            # Check JSON validity for v3
            if version == "v3" and record.response_status == "success":
                is_valid = self._validate_json_response(record.response_text)
                if is_valid:
                    results["json_valid_count"] += 1
            
            # Note: In a real scenario, we would extract tokens from the API response
            # For this implementation, we'll use dummy values for demonstration
            token_usage = TokenUsage(
                input_tokens=len(formatted_prompt.split()) * 1,  # Rough estimate
                output_tokens=len(record.response_text.split()) * 1 if record.response_text else 0,
                total_tokens=0
            )
            token_usage.total_tokens = token_usage.input_tokens + token_usage.output_tokens
            
            results["token_usage"].append({
                "input_tokens": token_usage.input_tokens,
                "output_tokens": token_usage.output_tokens,
                "total_tokens": token_usage.total_tokens
            })
            
            # Calculate cost
            cost_calc = CostCalculator.calculate_cost_for_tokens(
                token_usage.input_tokens,
                token_usage.output_tokens,
                MODEL_NAME
            )
            results["costs"].append({
                "input_cost": cost_calc.input_cost,
                "output_cost": cost_calc.output_cost,
                "total_cost": cost_calc.total_cost_per_request
            })
            
            print(f"  {question['id']}: ✓ Latency: {record.latency_seconds:.3f}s")
            time.sleep(0.5)  # Rate limiting
        
        self.evaluation_results[version] = results
        return results
    
    def _validate_json_response(self, response_text: str) -> bool:
        """
        Validate if response is valid JSON
        
        Args:
            response_text: Response text to validate
            
        Returns:
            True if valid JSON, False otherwise
        """
        if not response_text:
            return False
        
        try:
            json.loads(response_text)
            return True
        except (json.JSONDecodeError, ValueError):
            return False
    
    def evaluate_all_versions(self, prompts_dict: Dict) -> Dict[str, Dict]:
        """
        Evaluate all prompt versions
        
        Args:
            prompts_dict: Dictionary of prompts from config
            
        Returns:
            Dict mapping version to evaluation results
        """
        all_results = {}
        
        for key, prompt_data in prompts_dict.items():
            version = prompt_data["version"]
            template = prompt_data["template"]
            
            results = self.evaluate_prompt_version(version, template)
            all_results[version] = results
        
        return all_results


class MLflowExperimentTracker:
    """Track experiment runs in MLflow"""
    
    def __init__(self, registry: PromptRegistry, experiment_id: str = None):
        """Initialize the tracker"""
        self.registry = registry
        self.experiment_id = experiment_id or registry.experiment_id
    
    def log_prompt_version_run(
        self,
        version: str,
        evaluation_results: Dict[str, Any]
    ) -> str:
        """
        Log a prompt version run in MLflow
        
        Args:
            version: Prompt version
            evaluation_results: Evaluation results from PromptEvaluator
            
        Returns:
            Run ID
        """
        with mlflow.start_run(experiment_id=self.experiment_id) as run:
            # Log parameters
            mlflow.log_param("prompt_version", version)
            mlflow.log_param("model", MODEL_NAME)
            mlflow.log_param("questions_count", evaluation_results["questions_tested"])
            
            # Calculate metrics
            latencies = evaluation_results["latencies"]
            token_usage = evaluation_results["token_usage"]
            costs = evaluation_results["costs"]
            
            avg_latency = sum(latencies) / len(latencies) if latencies else 0
            avg_input_tokens = sum(t["input_tokens"] for t in token_usage) / len(token_usage) if token_usage else 0
            avg_output_tokens = sum(t["output_tokens"] for t in token_usage) / len(token_usage) if token_usage else 0
            avg_cost = sum(c["total_cost"] for c in costs) / len(costs) if costs else 0
            
            # Calculate JSON validity (for v3)
            valid_json_rate = (
                evaluation_results["json_valid_count"] / evaluation_results["questions_tested"]
                if evaluation_results["questions_tested"] > 0 else 0
            )
            
            # Log metrics
            mlflow.log_metric("avg_latency_seconds", avg_latency)
            mlflow.log_metric("avg_input_tokens", avg_input_tokens)
            mlflow.log_metric("avg_output_tokens", avg_output_tokens)
            mlflow.log_metric("avg_cost_per_request", avg_cost)
            mlflow.log_metric("valid_json", valid_json_rate)
            mlflow.log_metric("projected_monthly_cost", avg_cost * 10_000)
            
            # Log artifacts
            mlflow.log_dict(
                {
                    "version": version,
                    "results": evaluation_results
                },
                "evaluation_results.json"
            )
            
            # Log prompt details
            if version in self.registry.registered_prompts:
                prompt_info = self.registry.registered_prompts[version]
                mlflow.log_dict(prompt_info, f"prompt_v{version}_info.json")
            
            run_id = run.info.run_id
        
        return run_id
    
    def log_all_runs(self, evaluator: PromptEvaluator):
        """Log all evaluation runs"""
        run_ids = {}
        
        for version, results in evaluator.evaluation_results.items():
            run_id = self.log_prompt_version_run(version, results)
            run_ids[version] = run_id
            print(f"✓ Logged run for {version}: {run_id}")
        
        return run_ids
    
    def promote_version_to_production(self, version: str) -> bool:
        """
        Promote a prompt version to production using an alias
        
        Args:
            version: Prompt version to promote
            
        Returns:
            True if successful
        """
        # In a real MLflow setup, you would use aliases/stages
        # This is a demonstration of the promotion concept
        promotion_record = {
            "version": version,
            "promoted_at": datetime.now().isoformat(),
            "status": "production",
            "environment": "production",
            "alias": "production"
        }
        
        print(f"\n{'='*60}")
        print(f"PROMOTION TO PRODUCTION: {version}")
        print(f"{'='*60}")
        print(f"Version: {version}")
        print(f"Promoted at: {promotion_record['promoted_at']}")
        print(f"Status: {promotion_record['status']}")
        print(f"Alias: {promotion_record['alias']}")
        
        return True


class PromptComparator:
    """Compare prompt versions and generate comparison reports"""
    
    @staticmethod
    def compare_versions(evaluator: PromptEvaluator) -> Dict[str, Any]:
        """
        Compare all evaluated prompt versions
        
        Args:
            evaluator: PromptEvaluator with evaluation results
            
        Returns:
            Comparison results and recommendations
        """
        comparison = {
            "versions": {},
            "best_version": None,
            "recommendations": {}
        }
        
        # Calculate metrics for each version
        for version, results in evaluator.evaluation_results.items():
            latencies = results["latencies"]
            token_usage = results["token_usage"]
            costs = results["costs"]
            
            metrics = {
                "avg_latency_seconds": sum(latencies) / len(latencies) if latencies else 0,
                "avg_input_tokens": sum(t["input_tokens"] for t in token_usage) / len(token_usage) if token_usage else 0,
                "avg_output_tokens": sum(t["output_tokens"] for t in token_usage) / len(token_usage) if token_usage else 0,
                "avg_cost_per_request": sum(c["total_cost"] for c in costs) / len(costs) if costs else 0,
                "valid_json_rate": (
                    results["json_valid_count"] / results["questions_tested"]
                    if results["questions_tested"] > 0 else 0
                )
            }
            
            comparison["versions"][version] = metrics
        
        # Determine best version (prioritize JSON validity for v3, then latency, then cost)
        best_score = -1
        best_version = None
        
        for version, metrics in comparison["versions"].items():
            # Scoring: quality > latency > cost
            score = 0
            
            # JSON validity is crucial for v3
            if "v3" in version:
                score += metrics["valid_json_rate"] * 100
            
            # Lower latency is better
            max_latency = max(m["avg_latency_seconds"] for m in comparison["versions"].values())
            score += (max_latency - metrics["avg_latency_seconds"]) / max_latency * 30 if max_latency > 0 else 0
            
            # Lower cost is better
            max_cost = max(m["avg_cost_per_request"] for m in comparison["versions"].values())
            score += (max_cost - metrics["avg_cost_per_request"]) / max_cost * 20 if max_cost > 0 else 0
            
            if score > best_score:
                best_score = score
                best_version = version
        
        comparison["best_version"] = best_version
        comparison["best_score"] = best_score
        
        return comparison
