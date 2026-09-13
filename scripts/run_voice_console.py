from pathlib import Path

import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from services.voice.browser_gateway import router


ROOT = Path(__file__).resolve().parents[1]
VOICE_WEB = ROOT / "web" / "voice"


app = FastAPI(
    title="AEON MATRIX Thai Voice Console",
)

app.include_router(router)

app.mount(
    "/voice-static",
    StaticFiles(directory=str(VOICE_WEB)),
    name="voice-static",
)


@app.get("/")
async def root():
    return FileResponse(
        VOICE_WEB / "index.html"
    )


@app.get("/voice")
async def voice_console():
    return FileResponse(
        VOICE_WEB / "index.html"
    )


@app.get("/health")
async def health():
    return {
        "status": "READY",
        "language": "th-TH",
        "voice": "Kore",
        "voice_gateway": True,
        "governance_bypass": False,
        "transaction_execution": False,
    }


if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8080,
    )
