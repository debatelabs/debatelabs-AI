from openai import OpenAI
from fastapi import UploadFile
import logging
from io import BytesIO


class TranscriptionService:
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)

    async def preprocess_file(
            self, file: UploadFile
            ) -> BytesIO:
        try: 
            buffer =  BytesIO(await file.read())
            buffer.name = file.filename
            return buffer
        
        except Exception as e:
            logging.error(f"Failed to preprocess file: {e}")
            raise
    
    async def transcribe(
            self, file: UploadFile
            ) -> str:
        try:
            buffer = await self.preprocess_file(file)

            logging.info("Start transcribing")
            transcription = self.client.audio.transcriptions.create(
                model="gpt-4o-transcribe",
                file=buffer,
                response_format="text"
            )

        except Exception as e:
            logging.error(f"Transcription failed: {e}")
            raise

        logging.info("Finished transcribing")
        return transcription

