from fastapi import UploadFile, APIRouter, File
from fastapi.responses import JSONResponse
from src.transcriber.dependancies import TranscriberServiceDep


router = APIRouter()


@router.post("/transcribe")
async def transcribe(
    transcriber: TranscriberServiceDep,
    file: UploadFile = File(...),
) -> JSONResponse:
    """
    Transcribe the audio file.
    """
    transcription = await transcriber.transcribe(file)
    return JSONResponse(content=transcription, status_code=200)
