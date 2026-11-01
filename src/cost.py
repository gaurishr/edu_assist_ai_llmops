"""
Task 2: Token Counting and Cost Calculation Module

This module handles extracting token usage from API responses and calculating costs.
"""

from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from openai import OpenAI

# Handle both package imports (src.config) and direct imports (config)
try:
    from src.config import MODEL_PRICING, MODEL_NAME, CURRENCY
except ImportError:
    from config import MODEL_PRICING, MODEL_NAME, CURRENCY


@dataclass
class TokenUsage:
    """Token usage information from a single API request"""
    input_tokens: int
    output_tokens: int
    total_tokens: int


@dataclass
class CostCalculation:
    """Cost calculation for a single API request"""
    input_cost: float
    output_cost: float
    total_cost_per_request: float
    

class TokenCounter:
    """Handle token counting for LLM responses"""
    
    def __init__(self, model: str = MODEL_NAME):
        """Initialize the token counter"""
        self.model = model
        self.client = OpenAI()
    
    @staticmethod
    def extract_tokens_from_response(response) -> TokenUsage:
        """
        Extract token usage from an OpenAI API response
        
        Args:
            response: Response object from OpenAI API
            
        Returns:
            TokenUsage: Object containing token counts
        """
        return TokenUsage(
            input_tokens=response.usage.prompt_tokens,
            output_tokens=response.usage.completion_tokens,
            total_tokens=response.usage.total_tokens
        )
    
    @staticmethod
    def count_tokens_for_text(text: str, model: str = MODEL_NAME) -> int:
        """
        Estimate token count for text (without making an API call)
        Uses simple heuristic: ~4 characters per token
        
        Args:
            text: Text to count tokens for
            model: Model name (for future reference)
            
        Returns:
            Estimated token count
        """
        # Simple heuristic: approximately 4 characters per token
        # More accurate counting would require tiktoken library
        estimated_tokens = len(text) // 4
        return max(1, estimated_tokens)


class CostCalculator:
    """Calculate costs based on token usage and model pricing"""
    
    @staticmethod
    def calculate_cost_for_tokens(
        input_tokens: int,
        output_tokens: int,
        model: str = MODEL_NAME
    ) -> CostCalculation:
        """
        Calculate cost for given token counts
        
        Formula:
        Input Cost = Input Tokens / 1,000,000 × Input Price per Million Tokens
        Output Cost = Output Tokens / 1,000,000 × Output Price per Million Tokens
        Total Cost = Input Cost + Output Cost
        
        Args:
            input_tokens: Number of input tokens
            output_tokens: Number of output tokens
            model: Model name to use for pricing
            
        Returns:
            CostCalculation: Object containing cost breakdown
            
        Raises:
            ValueError: If model pricing is not found
        """
        if model not in MODEL_PRICING:
            raise ValueError(
                f"Pricing for model '{model}' not found. "
                f"Available models: {list(MODEL_PRICING.keys())}"
            )
        
        pricing = MODEL_PRICING[model]
        
        # Calculate costs
        input_cost = (input_tokens / 1_000_000) * pricing.input_price_per_million
        output_cost = (output_tokens / 1_000_000) * pricing.output_price_per_million
        total_cost = input_cost + output_cost
        
        return CostCalculation(
            input_cost=input_cost,
            output_cost=output_cost,
            total_cost_per_request=total_cost
        )
    
    @staticmethod
    def project_monthly_cost(
        average_cost_per_request: float,
        requests_per_month: int = 10_000
    ) -> float:
        """
        Project monthly cost based on average cost per request
        
        Args:
            average_cost_per_request: Average cost for one request
            requests_per_month: Number of requests per month (default: 10,000)
            
        Returns:
            Projected monthly cost in USD
        """
        return average_cost_per_request * requests_per_month
    
    @staticmethod
    def generate_cost_summary(
        cost_calculations: List[CostCalculation]
    ) -> Dict:
        """
        Generate summary statistics for a list of cost calculations
        
        Args:
            cost_calculations: List of CostCalculation objects
            
        Returns:
            Dict containing cost summary statistics
        """
        if not cost_calculations:
            return {}
        
        total_costs = [c.total_cost_per_request for c in cost_calculations]
        input_costs = [c.input_cost for c in cost_calculations]
        output_costs = [c.output_cost for c in cost_calculations]
        
        return {
            "average_cost_per_request": sum(total_costs) / len(total_costs),
            "total_cost_all_requests": sum(total_costs),
            "min_cost": min(total_costs),
            "max_cost": max(total_costs),
            "average_input_cost": sum(input_costs) / len(input_costs),
            "average_output_cost": sum(output_costs) / len(output_costs),
            "projected_monthly_cost_10k_requests": CostCalculator.project_monthly_cost(
                sum(total_costs) / len(total_costs)
            )
        }


class CostOptimizationAnalyzer:
    """Analyze cost optimization opportunities"""
    
    @staticmethod
    def recommend_optimizations(
        token_usage_list: List[Dict],
        cost_calculations: List[CostCalculation]
    ) -> List[str]:
        """
        Generate cost optimization recommendations
        
        Args:
            token_usage_list: List of token usage data
            cost_calculations: List of cost calculations
            
        Returns:
            List of optimization recommendations
        """
        recommendations = []
        
        # Calculate averages
        avg_input = sum(t.get("input_tokens", 0) for t in token_usage_list) / max(1, len(token_usage_list))
        avg_output = sum(t.get("output_tokens", 0) for t in token_usage_list) / max(1, len(token_usage_list))
        
        # Recommendation 1: Reduce context size
        if avg_input > 500:
            recommendations.append(
                "1. Reduce Context Size: Average input tokens are high ({:.0f}). "
                "Consider reducing retrieved context, shortening system prompts, "
                "or using query-specific context to lower input costs.".format(avg_input)
            )
        
        # Recommendation 2: Shorten responses
        if avg_output > 400:
            recommendations.append(
                "2. Shorten Responses: Average output tokens are high ({:.0f}). "
                "Add 'keep responses concise' instructions or use max_tokens "
                "parameter to limit output length and reduce costs.".format(avg_output)
            )
        
        # Recommendation 3: Cache stable content
        recommendations.append(
            "3. Implement Prompt Caching: For repeated queries with similar context, "
            "implement prompt caching at the API level to avoid re-processing stable "
            "system prompts and retrieved context (if using gpt-4-turbo or similar)."
        )
        
        # Recommendation 4: Model selection
        recommendations.append(
            "4. Model Optimization: Consider using gpt-3.5-turbo for simpler queries "
            "and evaluate gpt-4 only for complex tasks. For high-volume operations, "
            "evaluate cost vs. quality tradeoffs."
        )
        
        # Recommendation 5: Batch processing
        recommendations.append(
            "5. Batch Processing: If applicable, batch multiple queries into a single "
            "API call to reduce overhead and API invocation costs."
        )
        
        return recommendations if recommendations else [
            "Cost optimization opportunities: Monitor token usage patterns and "
            "consider caching, batch processing, or model selection optimization."
        ]
