from fastapi import Depends
from src.transcriber.service import TranscriptionService
from typing import Annotated
from openai import OpenAI


transcriber_service = TranscriptionService(client=OpenAI())
TranscriberServiceDep = Annotated[TranscriptionService, Depends(lambda: transcriber_service)]
