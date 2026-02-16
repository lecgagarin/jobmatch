from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse

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

    return {
        "message": "CV uploaded successfully",
        "filename": file.filename,
        "size_bytes": len(contents)
    }
