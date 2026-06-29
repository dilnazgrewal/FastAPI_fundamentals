from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):
    contents = await file.read()
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "size_bytes": len(contents),
    }
