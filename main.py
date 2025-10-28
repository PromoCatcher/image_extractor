from fastapi import FastAPI, status, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from schemas import ExtractingData
from image_downloader import download_images
from uploader import upload_images_to_gcs


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


@app.post("/extract-images", status_code=status.HTTP_201_CREATED)
async def extract_images(data: ExtractingData):
    try:
        await download_images(data.links, data.dates)
        upload_images_to_gcs(data.dates, data.store)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
    return "OK"
