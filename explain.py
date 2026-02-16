from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def explain_match(cv_text: str, job_description: str, score: int):

    prompt = f"""
    Explain the job match result briefly.

    Matching score: {score}%

    STRICT FORMAT:

    Why match:
    <max 2 short sentences>

    Strengths:
    • <bullet>
    • <bullet>
    • <bullet>

    Missing:
    • <bullet>
    • <bullet>
    • <bullet>

    Tips:
    • <bullet>
    • <bullet>

    RULES:
    - Keep it VERY SHORT; as you were a HR Manager
    - Clean UI-friendly formatting

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
