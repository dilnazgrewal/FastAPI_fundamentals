from fastapi import FastAPI, File, UploadFile
import shutil
from pathlib import Path

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

app = FastAPI()

@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):
    destination = UPLOAD_DIR / file.filename
    with destination.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename, "saved_to": str(destination)}

