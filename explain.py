from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def explain_match(cv_text: str, job_description: str, score: int):

    prompt = f"""
Explain the job match result.

Matching score: {score}%

USE EXACT FORMAT:

Why match:
- <short sentence>
- <short sentence>

Strengths:
• <short bullet>
• <short bullet>
• <short bullet>

Missing:
• <short bullet>
• <short bullet>
• <short bullet>

Tips:
• <short bullet>
• <short bullet>

STRICT RULES:
- No \\n characters
- No long paragraphs
- Short phrases only; as you vere HR Board member
- Clean UI formatting

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
