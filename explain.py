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
    - Keep it VERY SHORT
    - No extra commentary
    - No \\n characters
    - Clean UI-friendly formatting
    - Try to explain it as you were an HR manager, be concise

    CV:
    {cv_text}

    Job Description:
    {job_description}
    """
