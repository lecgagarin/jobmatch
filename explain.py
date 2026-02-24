from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_explanation(cv_text: str, job_description: str, score: int):

    prompt = f"""
Explain the job match result as you were a HR Board Member.

Matching score: {score}%

Return response EXACTLY like this template:

Why match:
- ...
- ...

Strengths:
- ...
- ...
- ...

Missing:
- ...
- ...
- ...

Tips:
- ...
- ...

Formatting rules:
- Preserve line breaks EXACTLY
- Each item on new line
- No paragraphs
- No extra commentary
- Plain professional language
- Executive / HR-style tone

CV:
{cv_text}

Job Description:
{job_description}
"""

    try:
        response = client.responses.create(
            model="gpt-5-mini",
            input=prompt
        )

        return response.output_text

    except Exception as e:
        return f"Explanation unavailable ({str(e)})"
