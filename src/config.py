"""
LLMOps Assignment 2: Configuration and Constants

This module defines constants and configuration for the LLMOps assignment,
including model details, API endpoints, and pricing information.
"""

import os
from typing import Dict
from dataclasses import dataclass
from datetime import datetime

# Load environment variables
from dotenv import load_dotenv

load_dotenv()

# API Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError(
        "OPENAI_API_KEY environment variable not set. "
        "Please set it before running the assignment."
    )

# Model Configuration
MODEL_NAME = "gpt-3.5-turbo"
API_VERSION = "2024-01-01"
PRICING_DATE = datetime.now().strftime("%Y-%m-%d")
CURRENCY = "USD"

@dataclass
class ModelPricing:
    """Model pricing information"""
    input_price_per_million: float
    output_price_per_million: float
    context_window: int
    
# Pricing for gpt-3.5-turbo (as of pricing_date)
# Source: https://openai.com/pricing
GPT_3_5_TURBO_PRICING = ModelPricing(
    input_price_per_million=0.50,  # $0.50 per 1M input tokens
    output_price_per_million=1.50,  # $1.50 per 1M output tokens
    context_window=4096
)

MODEL_PRICING: Dict[str, ModelPricing] = {
    "gpt-3.5-turbo": GPT_3_5_TURBO_PRICING,
}

# MLflow Configuration
MLFLOW_EXPERIMENT_NAME = "eduassist_llmops_assignment"
MLFLOW_TRACKING_URI = os.getenv("MLFLOW_TRACKING_URI", None)
MLFLOW_ARTIFACT_ROOT = os.getenv("MLFLOW_ARTIFACT_ROOT", "./mlruns")

# Test Questions
ACADEMIC_QUESTIONS = [
    {
        "id": "q1",
        "question": "What is photosynthesis and why is it important for life on Earth?"
    },
    {
        "id": "q2",
        "question": "Explain the difference between mitosis and meiosis."
    },
    {
        "id": "q3",
        "question": "What are the three main types of rocks and how are they formed?"
    },
    {
        "id": "q4",
        "question": "Describe the water cycle and its importance in the environment."
    },
    {
        "id": "q5",
        "question": "What is the significance of the Pythagorean theorem in mathematics?"
    }
]

# Prompt Versions
PROMPTS = {
    "v1_basic": {
        "version": "v1",
        "name": "Basic",
        "template": "Answer the following student question clearly.\nQuestion: {{question}}"
    },
    "v2_structured": {
        "version": "v2",
        "name": "Structured",
        "template": (
            "You are an academic assistant. "
            "Answer the following student question in a clear, concise, and accurate manner. "
            "Use simple language suitable for undergraduate students.\n"
            "Question: {{question}}"
        )
    },
    "v3_json": {
        "version": "v3",
        "name": "JSON Output",
        "template": (
            "You are an academic assistant. "
            "Answer the student question and return ONLY valid JSON. "
            "Do not include markdown, explanations outside JSON, or code fences.\n\n"
            "Use this exact JSON schema:\n"
            "{\n"
            '  "answer": "string",\n'
            '  "confidence": "high | medium | low",\n'
            '  "key_points": ["string"]\n'
            "}\n\n"
            "Question: {{question}}"
        )
    }
}

# Output paths
DATA_DIR = "data"
OUTPUTS_DIR = "outputs"
SCREENSHOTS_DIR = "screenshots"

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(OUTPUTS_DIR, exist_ok=True)
os.makedirs(SCREENSHOTS_DIR, exist_ok=True)

# Output file paths
LATENCY_TOKENS_COST_CSV = os.path.join(OUTPUTS_DIR, "latency_tokens_cost.csv")
PROMPT_EVALUATION_CSV = os.path.join(OUTPUTS_DIR, "prompt_evaluation_results.csv")
