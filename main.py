from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from schemas import ExtractingData


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/healt-check")
async def health_checking():
    return "Service healthy."


@app.post("/extract-images")
async def extract_images(data: ExtractingData):
    return "OK"
