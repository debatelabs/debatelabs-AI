from pydantic import BaseModel, Field


class Transcription(BaseModel):
    text: str = Field(..., description="The transcribed text from the audio file.")
