from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from cv_parser import extract_text_from_pdf
from ai_analysis import analyze_cv

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

    ai_result = analyze_cv(extracted_text)

    return {
        "message": "CV analyzed successfully",
        "filename": file.filename,
        "analysis": ai_result
    }
