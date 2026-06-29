import uuid
import shutil
from pathlib import Path
from fastapi import FastAPI, File, UploadFile

UPLOAD_DIR = Path("uploads")

app = FastAPI(title = "Learning UUID")
@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):
    # Generate a safe, server-controlled filename for the actual disk path
    extension = Path(file.filename).suffix  # e.g. ".pdf" — just the extension, no path
    safe_name = f"{uuid.uuid4()}{extension}"
    destination = UPLOAD_DIR / safe_name

    with destination.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "original_filename": file.filename, 
        "saved_as": safe_name,
    }