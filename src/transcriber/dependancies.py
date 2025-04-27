from fastapi import Depends
from src.transcriber.service import TranscriptionService
from typing import Annotated
from src.settings import settings


transcriber_service = TranscriptionService(api_key=settings.OPEN_AI_API_KEY)
TranscriberServiceDep = Annotated[TranscriptionService, Depends(lambda: transcriber_service)]
