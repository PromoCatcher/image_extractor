import pytest
import aiofiles
from image_downloader import save_file


@pytest.mark.asyncio
async def test_save_file(tmp_path):
    # Arrange
    test_content = b"hello world"
    test_file = tmp_path / "test.bin"

    # Act
    await save_file(test_content, str(test_file))

    # Assert: check file exists and has correct content
    assert test_file.exists(), "File should be created"

    async with aiofiles.open(test_file, "rb") as f:
        data = await f.read()

    assert data == test_content, "File content should match the input bytes"


@pytest.mark.asyncio
async def test_save_file_overwrites_existing(tmp_path):
    # Arrange
    test_file = tmp_path / "existing.bin"
    async with aiofiles.open(test_file, "wb") as f:
        await f.write(b"old content")

    # Act
    await save_file(b"new content", str(test_file))

    # Assert
    async with aiofiles.open(test_file, "rb") as f:
        data = await f.read()

    assert data == b"new content", "File should be overwritten with new data"
