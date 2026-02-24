from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import pdfplumber
import io

from matching import calculate_match_score, get_embedding
from explain import generate_explanation
from jobs_search import search_jobs   # ✅ poprawny import

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

    # ✅ JOB SEARCH (MVP MOCK)
    jobs = []

    for role in ["Finance Manager", "Senior Financial Analyst"]:
        jobs.extend(search_jobs(role))

    scored_jobs = []

    # ✅ FULL OPTIMIZED BLOCK 🚀🚀🚀
    for job in jobs:

        job_embedding = get_embedding(job["description"])  # ⭐ 1 call per job

        score = calculate_match_score(cv_embedding, job_embedding)  # ⚡ pure math

        scored_jobs.append({
            "title": job["title"],
            "company": job["company"],
            "description": job["description"],
            "match_score": score
        })

    # ✅ SORTING
    scored_jobs.sort(key=lambda x: x["match_score"], reverse=True)

    # ✅ EXPLAINABILITY — TOP 3 ONLY 🚀🔥
    for job in scored_jobs[:3]:
        job["explanation"] = generate_explanation(
            extracted_text,
            job["description"],
            job["match_score"]
        )

    # ✅ SPEED BOOST
    for job in scored_jobs[3:]:
        job["explanation"] = None

    return {
        "message": "CV analyzed successfully",
        "jobs_found": scored_jobs
    }
