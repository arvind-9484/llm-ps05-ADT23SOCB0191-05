# Social Media Caption Generator (PS #05)
**Name:** Arvind Pramod Malvade | **Enrollment No:** ADT23SOCB0191 | **Class:** LY-AIA-04 | **Roll No:** 05

## Problem Statement
Small creators spend time writing captions. This tool generates 3 tailored captions and hashtags each for Instagram, LinkedIn, and X (Twitter) from a short post description using a local LLM (`qwen2.5:3b` via Ollama).

## How to Run
1. Ensure Ollama is installed and pull the model: `ollama pull qwen2.5:3b`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the Streamlit app: `streamlit run app.py`