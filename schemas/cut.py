from pydantic import BaseModel

class Cut(BaseModel):
    # cutId: int
    style: str
