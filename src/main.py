from fastapi import FastAPI
from fastapi.responses import JSONResponse
from src.transcriber.router import router as transcriber_router


app = FastAPI()
app.include_router(transcriber_router, tags=["Transcriber"])


@app.get("/health", tags=["General"])
def health() -> JSONResponse:
    return JSONResponse(status_code=200, content={"health": "OK"})
