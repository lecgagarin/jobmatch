from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def explain_match(cv_text: str, job_description: str, score: int):

   prompt = f"""
Explain the job match result.

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
- No extra text
- No inline formatting
- Plain text only, as you are a HR Board Member

CV:
{cv_text}

Job Description:
{job_description}
"""

    try:
        response = client.chat.completions.create(
            model="gpt-5-mini",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Explanation unavailable ({str(e)})"
