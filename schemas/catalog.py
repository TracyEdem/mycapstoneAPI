from pydantic import BaseModel
from pathlib import Path

class Catalog(BaseModel):
    # catalogId: int
    cutId: int
    descriptor: str
    # image: Path
    # userId: int