from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import pdfplumber
import io

from matching import calculate_match_score, get_embedding
from explain import generate_explanation
from jobs import search_jobs  # Twoja funkcja API (Adzuna / Jooble / mock)

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
        extracted_text = "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())

    # ✅ EMBEDDING CV — TYLKO RAZ 🚀⭐⭐⭐⭐⭐
    cv_embedding = get_embedding(extracted_text)

    # ✅ JOB SEARCH
    jobs = get_jobs()  # np. Adzuna / Jooble

    scored_jobs = []

    for job in jobs:

        score = calculate_match_score(cv_embedding, job["description"])

        scored_jobs.append({
            "title": job["title"],
            "company": job["company"],
            "description": job["description"],
            "match_score": score
        })

    # ✅ SORTOWANIE
    scored_jobs.sort(key=lambda x: x["match_score"], reverse=True)

    # ✅ EXPLAINABILITY — tylko TOP 3 (jak miałeś)
    for job in scored_jobs[:3]:
        job["explanation"] = generate_explanation(extracted_text, job)

    # ✅ Reszta bez explanation (speed boost)
    for job in scored_jobs[3:]:
        job["explanation"] = None

    return {
        "message": "CV analyzed successfully",
        "jobs_found": scored_jobs
    }
