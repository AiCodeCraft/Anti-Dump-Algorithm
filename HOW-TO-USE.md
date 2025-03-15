# How to Use the Anti-Dump Algorithm to Calculate ADI (Anti-Dump Index)

> **Copyright 2008 - 2025 S. Volkan Kücükbudak**  
> _NOTE! THIS IS NOT AN APP! It is a demonstration of how to implement ADI. If you use this code, please read the LICENSE file. Respect free work of developers._

## Overview
The **Anti-Dump Algorithm** helps evaluate and filter low-quality inputs by calculating the **Anti-Dump Index (ADI)**. This guide explains how to:

1. Analyze input metrics (Noise, Effort, Context, Details, etc.).
2. Compute the ADI using a weighted formula.
3. Make decisions and generate recommendations for improving input quality.

This implementation can be integrated into AI tools, support systems, or any application requiring input quality assessment.

---

## Python Implementation

The core logic for calculating the ADI is implemented in the `adi.py` file. This file includes functions to analyze input text and compute the ADI.

### Key Features
1. **Metrics Extraction**:
   - **Noise**: Measures irrelevant content.
   - **Effort**: Evaluates clarity, structure, and punctuation.
   - **Context**: Assesses the presence of background information.
   - **Details**: Measures technical depth.
   - **Bonus Factors**: Rewards for well-formatted inputs.
   - **Penalty Factors**: Deductions for poor practices (e.g., excessive punctuation).

2. **Calculation Formula**:

```math
ADI = \frac{w_N \cdot \text{Noise} - (w_E \cdot \text{Effort} + w_B \cdot \text{BonusFactors})}{w_C \cdot \text{Context} + w_D \cdot \text{Details} + w_P \cdot \text{PenaltyFactors}}
```

3. **Decision Rules**:
   - **ADI > 1**: Reject input, ask for revision.
   - **0 ≤ ADI ≤ 1**: Medium-priority input.
   - **ADI < 0**: High-quality input, prioritize response.

---

## Example Code
### `adi.py`
This file contains the implementation of the Anti-Dump Algorithm. It includes functions to calculate noise, effort, context, details, bonus factors, and penalty factors, as well as to compute the ADI.
You can use the ADI as follows:
```python
from adi import DumpindexAnalyzer

# Initialisiere den ADI-Analyzer
analyzer = DumpindexAnalyzer()
```
[View `adi.py` Source Code](./adi.py)

### `example_app.py`
This file demonstrates how to use the `adi.py` implementation in a simple Flask application. It includes endpoints to analyze input text and return the ADI and recommendations.

[View `example_app.py` Source Code](./example_app.py)

---

## Key Steps for AI Integration
1. **Preprocessing**:
   - Analyze user input to extract metrics.
2. **ADI Calculation**:
   - Use the weights and formula to compute ADI.
3. **Decision Making**:
   - ADI > 1: Reject input.
   - 0 ≤ ADI ≤ 1: Medium priority.
   - ADI < 0: High priority.
4. **Feedback Loop**:
   - Provide recommendations for improving input quality based on detected issues.

---

**Stay Dump-Free!** 🚀

