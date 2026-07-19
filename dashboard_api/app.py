from fastapi import FastAPI
from executive_api.command_api import CommandAPI

app = FastAPI(
    title="AEON MATRIX Command Center",
    version="1.0"
)

api = CommandAPI()


@app.get("/")
def home():
    return {
        "system": "AEON MATRIX",
        "status": "ONLINE",
        "mode": "Sense > Think > Decide > Act > Learn"
    }


@app.get("/command-center")
def command_center():
    return api.status()
