from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from cv_parser import extract_text_from_pdf
from ai_analysis import analyze_cv
from jobs_search import search_jobs
from matching import calculate_match_score
from explain import explain_match

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Job Matcher API is running 🚀"}

@app.post("/upload-cv")
async def upload_cv(file: UploadFile = File(...)):
    
    if not file.filename.endswith(".pdf"):
        return JSONResponse(
            status_code=400,
            content={"error": "Only PDF files are allowed"}
        )

    contents = await file.read()
    extracted_text = extract_text_from_pdf(contents)

    analysis = analyze_cv(extracted_text)

    jobs = []

    for role in analysis["roles"][:3]:
        jobs.extend(search_jobs(role))

    scored_jobs = []

    for job in jobs:
        score = calculate_match_score(extracted_text, job["description"])

        explanation = explain_match(
            extracted_text,
            job["description"],
            score
        )

        scored_jobs.append({
            **job,
            "match_score": score,
            "explanation": explanation
        })

    return {
        "analysis": analysis,
        "jobs_found": scored_jobs
    }
