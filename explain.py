def explain_match(cv_text: str, job_description: str, score: int):

    prompt = f"""
    Explain the job match result briefly and concisely.

    Matching score: {score}%

    Respond in SHORT FORMAT:

    ✅ Why match (1–2 sentences)

    ✅ Strengths (max 3 bullet points)

    ✅ Missing / gaps (max 3 bullet points)

    ✅ Improvement tips (max 2 bullet points)

    Keep response VERY SHORT.

    CV:
    {cv_text}

    Job Description:
    {job_description}
    """
