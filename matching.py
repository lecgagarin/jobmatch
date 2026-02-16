from openai import OpenAI
import os
import math

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def cosine_similarity(vec1, vec2):
    dot = sum(a * b for a, b in zip(vec1, vec2))
    norm1 = math.sqrt(sum(a * a for a in vec1))
    norm2 = math.sqrt(sum(b * b for b in vec2))
    return dot / (norm1 * norm2)

def get_embedding(text: str):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding

def calculate_match_score(cv_text: str, job_description: str):

    cv_embedding = get_embedding(cv_text)
    job_embedding = get_embedding(job_description)

    similarity = cosine_similarity(cv_embedding, job_embedding)

    score = round(similarity * 100)

    return max(0, min(score, 100))
