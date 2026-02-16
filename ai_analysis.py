from openai import OpenAI
import os
import json

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_cv(cv_text: str):

    prompt = f"""
    Analyze the CV and return ONLY valid JSON.

    Do NOT include explanations.
    Do NOT include text outside JSON.

    {{
        "roles": [],
        "skills": [],
        "seniority": "",
        "summary": ""
    }}

    CV:
    {cv_text}
    """

    response = client.chat.completions.create(
        model="gpt-5-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    raw_output = response.choices[0].message.content

    try:
        return json.loads(raw_output)
    except:
        return {
            "roles": ["Parsing Error"],
            "skills": [],
            "seniority": "unknown",
            "summary": raw_output
        }
