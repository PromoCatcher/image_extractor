import os

from logger import logger
from google_config import bucket


def upload_images_to_gcs(date_range: str, store_name: str):
    logger.info("Getting all files")
    all_files = os.listdir(f"output/{date_range}")

    logger.info("Uploading files")
    for file in all_files:
        blob = bucket.blob(f"{store_name}/{date_range}/{file}")
        blob.upload_from_filename(f"output/{date_range}/{file}")

    logger.info("Files uploaded")
