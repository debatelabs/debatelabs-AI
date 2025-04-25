from fastapi import FastAPI, UploadFile, File, APIRouter, Depends
from src.transcriber.schemas import Transcription
from src.transcriber.service import TranscriptionService
from src.transcriber.dependancies import TranscriberServiceDep


router = APIRouter()


@router.post("/transcribe")
async def transcribe(
    audio: UploadFile,
    transcriber: TranscriberServiceDep
    ) -> Transcription:
    """
    Transcribe the audio file to text.
    """
    transcription = await transcriber.transcribe(audio)
    return Transcription(text=transcription)
    