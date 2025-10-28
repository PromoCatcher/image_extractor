import os
import httpx
import aiofiles

from logger import logger


async def get_image_content(image_link: str) -> bytes:
    async with httpx.AsyncClient() as client:
        resp = await client.get(image_link)
        return resp.content


async def save_file(content: bytes, file_path: str):
    async with aiofiles.open(file_path, "wb") as file:
        await file.write(content)


async def download_images(image_links: list[str], dates: str):
    logger.info("Check is the folder existing")
    os.makedirs("output", exist_ok=True)
    os.makedirs(f"output/{dates}", exist_ok=True)

    logger.info("Start get the images")
    for i, link in enumerate(image_links):
        logger.info(f"Get image with link {link}")
        await save_file(await get_image_content(link), f"output/{dates}/page_{i}.jpg")
        logger.info("Image downloaded")

    logger.info("Downloading images finished")
