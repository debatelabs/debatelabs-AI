from openai import OpenAI
from fastapi import UploadFile
import logging
from io import BytesIO
from .config import ALLOWED_AUDIO_TYPES
from .exceptions import InvalidAudioType
from .schemas import Transcription


# TODO: Decouple the allowed audio types
# TODO: Decouple preprocessing and validation logic
class TranscriptionService:
    def __init__(self, api_key: str) -> None:
        self.client = OpenAI(api_key=api_key)

    def _validate_audio_file(self, file: UploadFile) -> None:
        """
        Checks if file is a valid audio.
        """
        if not file.content_type in ALLOWED_AUDIO_TYPES:
            logging.error(f"Invalid audio type {file.content_type}")
            raise InvalidAudioType()

    async def _preprocess_file(
        self,
        file: UploadFile,
    ) -> BytesIO:
        try:
            buffer = BytesIO(await file.read())
            buffer.name = file.filename
            return buffer

        except Exception as e:
            logging.error(f"Failed to preprocess file: {e}")
            raise

    async def transcribe(self, file: UploadFile) -> Transcription:

        try:
            # Validate file
            self._validate_audio_file(file)

            # Preprocess audio file
            buffer = await self._preprocess_file(file)

            logging.info("Start transcribing")
            text = self.client.audio.transcriptions.create(
                model="gpt-4o-transcribe", file=buffer, response_format="text"
            )

            transcription = Transcription(text=text)

        except Exception as e:
            logging.error(f"Transcription failed: {e}")
            raise

        logging.info("Finished transcribing")

        return transcription.model_dump_json()
