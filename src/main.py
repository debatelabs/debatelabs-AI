from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from src.transcriber.schemas import Transcription
from src.transcriber.router import router as transcriber_router

app = FastAPI()
app.include_router(transcriber_router, prefix="/transcriber", tags=["Transcriber"])

@app.get("/")
async def health():
    return JSONResponse(
        status_code=200, content={"health": "OK"}
        )


