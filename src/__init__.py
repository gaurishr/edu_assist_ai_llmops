"""
MLOps Assignment 2 - LLMOps: API Cost, Latency, and Prompt Version Management
src package
"""

__version__ = "1.0.0"
__author__ = "Gauri Shanker"

from .config import (
    OPENAI_API_KEY,
    MODEL_NAME,
    ACADEMIC_QUESTIONS,
    PROMPTS,
    MLFLOW_EXPERIMENT_NAME
)

from .latency import (
    LLMAPIClient,
    LatencyAnalyzer,
    LatencyRecord
)

from .cost import (
    TokenCounter,
    CostCalculator,
    CostOptimizationAnalyzer,
    TokenUsage,
    CostCalculation
)

from .mlflow_manager import (
    PromptRegistry,
    PromptEvaluator,
    MLflowExperimentTracker,
    PromptComparator
)

__all__ = [
    "OPENAI_API_KEY",
    "MODEL_NAME",
    "ACADEMIC_QUESTIONS",
    "PROMPTS",
    "MLFLOW_EXPERIMENT_NAME",
    "LLMAPIClient",
    "LatencyAnalyzer",
    "LatencyRecord",
    "TokenCounter",
    "CostCalculator",
    "CostOptimizationAnalyzer",
    "TokenUsage",
    "CostCalculation",
    "PromptRegistry",
    "PromptEvaluator",
    "MLflowExperimentTracker",
    "PromptComparator"
]
