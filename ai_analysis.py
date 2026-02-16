from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_cv(cv_text: str):

    prompt = f"""
    Analyze the following CV.

    Extract:

    1. Most likely job roles
    2. Key skills
    3. Seniority level
    4. Short professional summary

    CV:
    {cv_text}
    """

    response = client.chat.completions.create(
        model="gpt-5-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
