from fastapi import UploadFile, APIRouter, File
from src.transcriber.schemas import Transcription
from src.transcriber.dependancies import TranscriberServiceDep


router = APIRouter()


@router.post("/transcribe")
async def transcribe(
    transcriber: TranscriberServiceDep, file: UploadFile = File(...), 
    ) -> Transcription:
    """
    Transcribe the audio file.
    """
    transcription = await transcriber.transcribe(file)
    return Transcription(text=transcription)
    