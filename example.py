# NOTE! THIS IS NOT AN APP!
# IT SHOWS YOU HOW YOU CAN USE ADI - MAYBE FOR YOUR AI TOOLS
# ==== IF YOU USE MY CODE READ LICENSE FILE PLEASE ====
# DONT STEAL FREE CODE FROM OTHERS! RESPECT FREE WORK OF DEVELOPERS AND THEIR CREDITS OR IN FUTURE YOU MUST PAY FOR CODE LIKE THIS!
# ==== Copyright 2008 - 2025 S. Volkan Kücükbudak ====

# Import necessary libraries
from dataclasses import dataclass
from typing import List, Dict, Tuple
import re
from collections import Counter
import numpy as np

# Define InputMetrics class to store metrics for evaluation
@dataclass
class InputMetrics:
    noise: float
    effort: float
    context: float
    details: float
    bonus_factors: float
    penalty_factors: float

# DumpIndexAnalyzer class to analyze inputs based on ADI logic
class DumpindexAnalyzer:
    def __init__(self, weights: Dict[str, float] = None):
        # Default weights for different metrics in ADI calculation
        self.weights = weights or {
            'noise': 1.0,
            'effort': 2.0,
            'context': 1.5,
            'details': 1.5,
            'bonus': 0.5,
            'penalty': 1.0
        }
        
        # Patterns for identifying "Noise" elements in text
        self.noise_patterns = {
            'urgency': r'\b(urgent|asap|emergency|!!+|\?\?+)\b',
            'informal': r'\b(pls|plz|thx)\b',
            'vague': r'\b(something|somehow|maybe|probably)\b'
        }
        
        # Patterns to identify technical details
        self.detail_patterns = {
            'code_elements': r'\b(function|class|method|variable|array|object)\b',
            'technical_terms': r'\b(error|exception|bug|issue|crash|fail)\b',
            'specifics': r'[a-zA-Z_][a-zA-Z0-9_]*\.[a-zA-Z_][a-zA-Z0-9_]*'
        }

    def calculate_noise(self, text: str) -> Tuple[float, Dict]:
        """
        Calculate the noise in the input text by identifying patterns such as urgency, informality, and vagueness.
        Returns the noise ratio and details of matches.
        """
        noise_count = 0
        noise_details = {}
        
        for category, pattern in self.noise_patterns.items():
            matches = re.findall(pattern, text.lower())
            noise_count += len(matches)
            noise_details[category] = matches
        
        total_words = len(text.split())
        return (noise_count / max(total_words, 1), noise_details)

    def calculate_effort(self, text: str) -> float:
        """
        Evaluate the effort put into structuring the input.
        Includes sentence length, formatting, and punctuation.
        """
        sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
        if not sentences:
            return 0.0
        
        avg_sentence_length = np.mean([len(s.split()) for s in sentences])
        has_formatting = bool(re.search(r'```|\*\*|\n\s*\n', text))
        has_punctuation = bool(re.search(r'[.,;:]', text))
        
        effort_score = min(5.0, (
            (20 <= avg_sentence_length <= 50) * 2.0 +
            has_formatting * 1.5 +
            has_punctuation * 1.5
        ))
        
        return effort_score

    def calculate_context(self, text: str) -> float:
        """
        Evaluate the context provided in the input.
        Identifies indicators such as background, environment, or goal statements.
        """
        context_indicators = {
            'background': r'\b(because|since|as|when|while)\b',
            'environment': r'\b(using|version|environment|platform|system)\b',
            'goal': r'\b(trying to|want to|need to|goal is|attempting to)\b'
        }
        
        context_score = 0.0
        for category, pattern in context_indicators.items():
            if re.search(pattern, text.lower()):
                context_score += 1.0
                
        return min(5.0, context_score)

    def calculate_details(self, text: str) -> Tuple[float, Dict]:
        """
        Evaluate the level of technical details provided in the input.
        Returns a score and the details identified.
        """
        detail_score = 0.0
        detail_findings = {}
        
        for category, pattern in self.detail_patterns.items():
            matches = re.findall(pattern, text)
            score = len(matches) * 0.5
            detail_findings[category] = matches
            detail_score += score
            
        return (min(5.0, detail_score), detail_findings)

    def calculate_bonus_factors(self, text: str) -> float:
        """
        Identify and score bonus factors such as code blocks, links, and structured lists.
        """
        bonus_score = 0.0
        
        if re.search(r'```[\s\S]*?```', text):
            bonus_score += 1.0
        if re.search(r'\[.*?\]\(.*?\)', text):
            bonus_score += 0.5
        if re.search(r'\n\s*[-*+]\s', text):
            bonus_score += 0.5
        
        return bonus_score

    def calculate_penalty_factors(self, text: str) -> Tuple[float, Dict]:
        """
        Identify penalties for issues such as excessive capitalization, punctuation, or very short inputs.
        Returns a penalty score and details of penalties.
        """
        penalties = {}
        
        caps_ratio = len(re.findall(r'[A-Z]', text)) / max(len(re.findall(r'[a-zA-Z]', text)), 1)
        if caps_ratio > 0.7:
            penalties['excessive_caps'] = caps_ratio
        
        excessive_punctuation = len(re.findall(r'[!?]{2,}', text))
        if excessive_punctuation:
            penalties['excessive_punctuation'] = excessive_punctuation
        
        if len(text.split()) < 10:
            penalties['too_short'] = True
        
        penalty_score = min(5.0, sum(penalties.values()) if penalties else 0)
        return (penalty_score, penalties)

    def calculate_adi(self, metrics: InputMetrics) -> float:
        """
        Calculate the Anti-Dump Index (ADI) using the provided metrics and weights.
        """
        try:
            numerator = (
                self.weights['noise'] * metrics.noise -
                (self.weights['effort'] * metrics.effort +
                 self.weights['bonus'] * metrics.bonus_factors)
            )
            denominator = (
                self.weights['context'] * metrics.context +
                self.weights['details'] * metrics.details +
                self.weights['penalty'] * metrics.penalty_factors
            )
            return numerator / max(denominator, 0.1)
        except Exception as e:
            print(f"Error calculating ADI: {e}")
            return float('inf')

   def analyze_input(self, text: str) -> Dict:
        """
        Analyze the input text and return the calculated ADI, metrics, decisions, and recommendations.
        """
        noise_value, noise_details = self.calculate_noise(text)
        effort_value = self.calculate_effort(text)
        context_value = self.calculate_context(text)
        details_value, detail_findings = self.calculate_details(text)
        bonus_value = self.calculate_bonus_factors(text)
        penalty_value, penalty_details = self.calculate_penalty_factors(text)
            
        metrics = InputMetrics(
            noise=noise_value,
            effort=effort_value,
            context=context_value,
            details=details_value,
            bonus_factors=bonus_value,
            penalty_factors=penalty_value
        )
            
        adi = self.calculate_adi(metrics)
            
        decision = self._make_decision(adi)
        recommendations = self._generate_recommendations(metrics, noise_details, detail_findings, penalty_details)
            
        return {
            'adi': round(adi, 3),
            'metrics': {
                'noise': round(noise_value, 3),
                'effort': round(effort_value, 3),
                'context': round(context_value, 3),
                'details': round(details_value, 3),
                'bonus_factors': round(bonus_value, 3),
                'penalty_factors': round(penalty_value, 3)
            },
            'decision': decision,
            'recommendations': recommendations,
                details': {
                'noise_findings': noise_details,
                'technical_details': detail_findings,
                'penalties': penalty_details
            }
        }

    def _make_decision(self, adi: float) -> str:
        """
        Make a decision based on the calculated ADI value.
         """
        if adi > 1:
            return "REJECT"
        elif 0 <= adi <= 1:
            return "MEDIUM_PRIORITY"
        else:
            return "HIGH_PRIORITY"

    def _generate_recommendations(self, metrics: InputMetrics, 
                                noise_details: Dict, 
                                detail_findings: Dict,
                                penalty_details: Dict) -> List[str]:
        """
        Generate recommendations for improving the input based on the metrics and findings.
        """
        recommendations = []
            
        if metrics.noise > 0.3:
            recommendations.append("Reduce informal or urgent expressions.")
                
        if metrics.context < 1.0:
            recommendations.append("Provide more context (environment, background, goal).")
                
        if metrics.details < 1.0:
            recommendations.append("Include specific technical details.")
                
        if metrics.effort < 2.0:
            recommendations.append("Improve the structure of your input.")
                
        if metrics.penalty_factors > 0:
            if 'excessive_caps' in penalty_details:
                recommendations.append("Avoid excessive capitalization.")
            if 'excessive_punctuation' in penalty_details:
                recommendations.append("Reduce excessive punctuation marks.")
            if 'too_short' in penalty_details:
                recommendations.append("Provide a more detailed description.")
                    
        return recommendations

# END

# =====================================================================================================
# Example usage
# =====================================================================================================
analyzer = DumpindexAnalyzer()

# Testwith different inputs
test_inputs = [
    "Pls fix my code. Urgent!!!",
    """I'm trying to implement a login function in Python. 
    When calling auth.login(), I get a TypeError. 
    Here's my code:
    ```python
    def login(username, password):
        return auth.login(username)
    ```
    I'm using Python 3.8 and the auth library version 2.1."""
]

for input_text in test_inputs:
    result = analyzer.analyze_input(input_text)
    print(f"\nAnalyse für: {input_text[:50]}...")
    print(f"ADI: {result['adi']}")
    print(f"Entscheidung: {result['decision']}")
    print("Empfehlungen:")
    for rec in result['recommendations']:
        print(f"- {rec}")
    print("\nMetriken:", result['metrics'])
