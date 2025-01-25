# The Anti-Dump Algorithm

$$
\text{Komplexitätsindex} 
= \frac{\text{Systemkomplexität} \cdot \text{Variablen}}
       {\text{Verständlichkeit} + \text{Dokumentation}}
$$

If you develop AI tools, you’ve probably encountered how surprisingly unproductive or nonsensical some human input can be. These "dumpy" requests waste both time and money! After extensive testing, I realized that filtering such input was no easy task. Large Language Models (LLMs) often provide answers to even the most irrelevant or unclear queries. So, I thought: why not solve this problem with math? And that’s exactly what happened!

## Purpose
The **Anti-Dump Algorithm** calculates the **ADI (Anti-Dump Index)**. It is specifically designed to evaluate and filter out unproductive or irrelevant input—commonly referred to as "noise"—while prioritizing clarity, effort, and context. This algorithm measures the quality of input based on several key parameters, ensuring only meaningful contributions are processed.

#### Calculate Anti-Dump Index (ADI)
![AntiDumpIndex](adi-universal.jpg)

###### LaTeX Code:
$$
ADI = \frac{w_N \cdot \text{Noise} - (w_E \cdot \text{Effort} + w_B \cdot \text{BonusFactors})}{w_C \cdot \text{Context} + w_D \cdot \text{Details} + w_P \cdot \text{PenaltyFactors}}
$$

## Formula

The Basic parameters
$$

\text{DumpIndex} 
= \frac{\text{Noise} - \text{Effort}}
{\text{Context} + \text{Details}}
$$

### Parameters:
1. **Noise (N):**
   - Represents irrelevant or redundant parts of the input.
   - Includes filler words (e.g., "pls," "ASAP," excessive punctuation) and overuse of complex terms without context.
   
2. **Effort (E):**
   - Measures the clarity and structure of the input.
   - High-effort inputs include well-written sentences and proper formatting.

3. **Context (C):**
   - Refers to the presence of relevant background information (e.g., system specs, problem environment).

4. **Details (D):**
   - Captures the depth of technical information provided (e.g., specific error messages, code snippets).

---

## Adjusted Noise Calculation
To refine the Noise parameter:

\[
\text{Noise}_{\text{Adjusted}} = \text{Noise} \cdot \left(1 - \frac{\text{Details}}{\text{Total Words}}\right)
\]

This adjustment reduces Noise for inputs with substantial details.

---

## Pseudo-Competence Filtering
To identify "pseudo-competence" (e.g., overly complex language without substance):

\[
\text{ProfilierungsIndex} = \frac{\text{PseudoFachbegriffe} + \text{Noise}}{\text{Effort} + \text{Details}}
\]

A high ProfilierungsIndex indicates inputs with more noise than meaningful content.

---

## Quality Assessment
For more precise evaluation, we introduce the **Anti-Dump Score**:

\[
\text{AntiDumpScore} = \frac{\text{Effort} + \text{Context} + \text{Details}}{\text{Noise} + 1}
\]

- High AntiDumpScore = High-quality input.
- Low AntiDumpScore = Poor-quality input.

---

## Examples

### Example 1: "Fix my code pls!"
**Input:**
```
Pls fix my code! It doesn't work!!!
```

- **Noise:** 4 irrelevant words.
- **Effort:** 0 (no structure or useful detail).
- **Context:** 0.
- **Details:** 0.

\[
\text{DumpIndex} = \frac{4 - 0}{0 + 0} = \infty
\]
**Result:** Full rejection.

---

### Example 2: "SyntaxError in Python"
**Input:**
```
I get a SyntaxError in Python. Here's my code snippet.
```

- **Noise:** 0.
- **Effort:** 2 (clear description).
- **Context:** 1 (mention of Python).
- **Details:** 1 (specific error).

\[
\text{DumpIndex} = \frac{0 - 2}{1 + 1} = -1
\]
**Result:** Accepted.

---

## Visualization
### Zones
- **DumpZone:** \( \text{DumpIndex} > 1 \)
- **GrayArea:** \( 0 \leq \text{DumpIndex} \leq 1 \)
- **GeniusZone:** \( \text{DumpIndex} < 0 \)

---

## Applications
- **Support Systems:** Filter low-effort tickets.
- **Education:** Grade quality of student submissions.
- **HR:** Screen candidates' application clarity.

---

## Final Note
The Anti-Dump Algorithm isn’t just about filtering—it’s about promoting better communication and thoughtful input. 🚀
