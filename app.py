import os
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from main import generate_brochure

app = FastAPI()

# Mount static files for the frontend
app.mount("/static", StaticFiles(directory="static"), name="static")

class BrochureRequest(BaseModel):
    url: str

@app.post("/api/brochure")
async def create_brochure(request: BrochureRequest):
    try:
        # Call the existing logic from main.py
        result = generate_brochure(request.url)
        return {"markdown": result}
    except Exception as e:
        print(f"Error generating brochure: {e}")
        raise HTTPException(status_code=500, detail=str(e))

from fastapi.responses import FileResponse

@app.get("/")
async def read_root():
    return FileResponse('static/index.html')
