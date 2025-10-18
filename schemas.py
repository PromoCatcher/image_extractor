from pydantic import BaseModel


class ExtractingData(BaseModel):
    store: str
    dates: str
    links: list[str]
