from os import environ

import pytest
from httpx import Response, Request

from image_downloader import get_image_content


@pytest.mark.asyncio
async def test_get_image_content_success(monkeypatch):
    fake_bytes = b"Fake_image_data"

    async def mock_get(self, url, *args, **kwargs):
        request = Request("GET", url)
        return Response(200, content=fake_bytes, request=request)

    monkeypatch.setattr("httpx.AsyncClient.get", mock_get)

    content = await get_image_content("https://example.com/image.png")

    assert content == fake_bytes


@pytest.mark.skipif(
    environ.get("TEST_LEVEL") != "integration", reason="Integration test"
)
@pytest.mark.asyncio
async def test_get_image_content_integration():
    content = await get_image_content(
        "https://upload.wikimedia.org/wikipedia/commons/6/63/Wikipedia-logo.png"
    )

    assert isinstance(content, bytes)
    assert len(content) > 0

    assert content[:4] == b"\x89PNG"
