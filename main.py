from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import pdfplumber
import io

from matching import calculate_match_score, get_embedding, get_embeddings_batch
from explain import generate_explanation
from jobs_search import search_jobs

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"status": "Job Matcher API is running 🚀"}

@app.post("/upload-cv")
async def upload_cv(file: UploadFile = File(...)):

    contents = await file.read()

    # ✅ PDF EXTRACTION
    with pdfplumber.open(io.BytesIO(contents)) as pdf:
        extracted_text = "\n".join(
            page.extract_text() for page in pdf.pages if page.extract_text()
        )

    # ✅ CV EMBEDDING — ONLY ONCE 🚀🔥
    cv_embedding = get_embedding(extracted_text)

    # ✅ JOB SEARCH
    jobs = []

    for role in ["Finance Manager", "Senior Financial Analyst"]:
        jobs.extend(search_jobs(role))

    if not jobs:
        return {"message": "No jobs found"}

    # ✅ ⭐⭐⭐ BATCH JOB EMBEDDINGS ⭐⭐⭐
    job_descriptions = [job["description"] for job in jobs]
    job_embeddings = get_embeddings_batch(job_descriptions)

    scored_jobs = []

    # ✅ ULTRA FAST LOOP 🚀🔥
    for job, job_embedding in zip(jobs, job_embeddings):

        score = calculate_match_score(cv_embedding, job_embedding)

        scored_jobs.append({
            "title": job["title"],
            "company": job["company"],
            "description": job["description"],
            "match_score": score
        })

    # ✅ SORTING
    scored_jobs.sort(key=lambda x: x["match_score"], reverse=True)

    # ✅ ONLY BEST MATCH EXPLANATION ⭐⭐⭐
    best_job = scored_jobs[0]

    best_job["explanation"] = generate_explanation(
        extracted_text,
        best_job["description"],
        best_job["match_score"]
    )

    for job in scored_jobs[1:]:
        job["explanation"] = None

    return {
        "message": "CV analyzed successfully",
        "jobs_found": scored_jobs
    }
