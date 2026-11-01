"""
Task 1: API Call and Latency Measurement Module

This module handles calling LLM APIs and measuring latency for each request.
"""

import json
import time
from datetime import datetime
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, asdict
import requests
from openai import OpenAI

from .config import (
    OPENAI_API_KEY, 
    MODEL_NAME, 
    ACADEMIC_QUESTIONS,
    PROMPTS
)


@dataclass
class LatencyRecord:
    """Record for a single API call with latency measurements"""
    question_id: str
    question: str
    prompt_version: str
    model_name: str
    start_time: float
    end_time: float
    latency_seconds: float
    response_status: str
    response_text: Optional[str] = None
    error_message: Optional[str] = None
    timestamp: Optional[str] = None


class LLMAPIClient:
    """Client for calling LLM APIs and measuring performance"""
    
    def __init__(self, api_key: str = None, model: str = MODEL_NAME):
        """Initialize the LLM API client"""
        self.api_key = api_key or OPENAI_API_KEY
        self.model = model
        self.client = OpenAI(api_key=self.api_key)
        self.latency_records: List[LatencyRecord] = []
    
    def call_api(
        self, 
        prompt: str, 
        question_id: str, 
        prompt_version: str,
        temperature: float = 0.7,
        max_tokens: int = 500
    ) -> LatencyRecord:
        """
        Call the LLM API and measure latency
        
        Args:
            prompt: The formatted prompt to send to the model
            question_id: ID of the question being asked
            prompt_version: Version of the prompt (v1, v2, v3)
            temperature: Sampling temperature (0.0 to 2.0)
            max_tokens: Maximum tokens in response
            
        Returns:
            LatencyRecord: Record containing latency and response data
        """
        question = next(
            (q["question"] for q in ACADEMIC_QUESTIONS if q["id"] == question_id),
            "Unknown question"
        )
        
        # Record start time
        start_time = time.time()
        start_timestamp = datetime.now().isoformat()
        
        try:
            # Call the API
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=temperature,
                max_tokens=max_tokens
            )
            
            # Record end time
            end_time = time.time()
            latency = end_time - start_time
            
            # Extract response
            response_text = response.choices[0].message.content
            
            # Create record
            record = LatencyRecord(
                question_id=question_id,
                question=question,
                prompt_version=prompt_version,
                model_name=self.model,
                start_time=start_time,
                end_time=end_time,
                latency_seconds=latency,
                response_status="success",
                response_text=response_text,
                timestamp=start_timestamp
            )
            
            self.latency_records.append(record)
            return record
            
        except Exception as e:
            # Record end time
            end_time = time.time()
            latency = end_time - start_time
            
            # Create error record
            record = LatencyRecord(
                question_id=question_id,
                question=question,
                prompt_version=prompt_version,
                model_name=self.model,
                start_time=start_time,
                end_time=end_time,
                latency_seconds=latency,
                response_status="error",
                error_message=str(e),
                timestamp=start_timestamp
            )
            
            self.latency_records.append(record)
            return record
    
    def test_latency_for_all_questions(self, prompt_version: str = "v1") -> List[LatencyRecord]:
        """
        Test latency for all academic questions with a given prompt version
        
        Args:
            prompt_version: Version of the prompt to test (v1, v2, v3)
            
        Returns:
            List[LatencyRecord]: List of latency records for all questions
        """
        records = []
        # Map prompt version names to actual keys
        prompt_key_map = {
            "v1_basic": "v1_basic",
            "v2_structured": "v2_structured",
            "v3_json": "v3_json",
            "v1": "v1_basic",      # Allow short names too
            "v2": "v2_structured",
            "v3": "v3_json"
        }
        
        if prompt_version not in prompt_key_map:
            raise ValueError(f"Unknown prompt version: {prompt_version}. Available: {list(prompt_key_map.keys())}")
        
        prompt_key = prompt_key_map[prompt_version]
        prompt_template = PROMPTS[prompt_key]["template"]
        
        for question in ACADEMIC_QUESTIONS:
            # Format prompt with the question
            formatted_prompt = prompt_template.replace(
                "{{question}}", 
                question["question"]
            )
            
            # Call API
            record = self.call_api(
                prompt=formatted_prompt,
                question_id=question["id"],
                prompt_version=prompt_version
            )
            records.append(record)
            
            # Add small delay between requests to avoid rate limiting
            time.sleep(0.5)
        
        return records


class LatencyAnalyzer:
    """Analyze latency statistics from API calls"""
    
    @staticmethod
    def calculate_statistics(latencies: List[float]) -> Dict[str, float]:
        """
        Calculate latency statistics
        
        Args:
            latencies: List of latency values in seconds
            
        Returns:
            Dict containing mean, median, min, max, and std dev
        """
        import statistics
        
        if not latencies:
            return {}
        
        sorted_latencies = sorted(latencies)
        
        stats = {
            "count": len(latencies),
            "mean_seconds": statistics.mean(latencies),
            "median_seconds": statistics.median(latencies),
            "min_seconds": min(latencies),
            "max_seconds": max(latencies),
            "stdev_seconds": statistics.stdev(latencies) if len(latencies) > 1 else 0.0
        }
        
        return stats
    
    @staticmethod
    def analyze_records(records: List[LatencyRecord]) -> Dict[str, Any]:
        """
        Analyze a list of latency records
        
        Args:
            records: List of LatencyRecord objects
            
        Returns:
            Dict containing analysis results
        """
        successful_records = [r for r in records if r.response_status == "success"]
        error_records = [r for r in records if r.response_status == "error"]
        
        latencies = [r.latency_seconds for r in successful_records]
        
        analysis = {
            "total_requests": len(records),
            "successful_requests": len(successful_records),
            "failed_requests": len(error_records),
            "latency_stats": LatencyAnalyzer.calculate_statistics(latencies),
            "error_messages": [r.error_message for r in error_records if r.error_message]
        }
        
        # Find slowest request
        if successful_records:
            slowest = max(successful_records, key=lambda r: r.latency_seconds)
            analysis["slowest_request"] = {
                "question_id": slowest.question_id,
                "latency_seconds": slowest.latency_seconds,
                "question": slowest.question[:100] + "..." if len(slowest.question) > 100 else slowest.question
            }
        
        return analysis
