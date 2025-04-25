from openai import OpenAI
from fastapi import UploadFile


class TranscriptionService:
    def __init__(self, client: OpenAI):
        self.client = client

    async def transcribe(self, audio_file: UploadFile) -> str:
        transcription = self.client.audio.transcriptions.create(
            model="gpt-4o-transcribe",
            file=audio_file.file,
            response_format="text"
        )
        return transcription

