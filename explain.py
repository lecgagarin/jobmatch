from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def explain_match(cv_text: str, job_description: str, score: int):

    prompt = f"""
    Explain the job match result briefly and concisely.

    Matching score: {score}%

    Respond in SHORT FORMAT:

    Why match (1–2 short sentences)

    Strengths (max 3 bullet points)

    Missing / gaps (max 3 bullet points)

    Improvement tips (max 2 bullet points)

    Keep response VERY SHORT and UI-friendly.

    CV:
    {cv_text}

    Job Description:
    {job_description}
    """

    response = client.chat.completions.create(
        model="gpt-5-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
