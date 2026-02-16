from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def explain_match(cv_text: str, job_description: str, score: int):

    prompt = f"""
    Explain the job match result.

    Matching score: {score}%

    Provide:

    1. Why this job is a good / bad match
    2. Key matching strengths
    3. Missing skills or gaps
    4. Short improvement suggestions

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
