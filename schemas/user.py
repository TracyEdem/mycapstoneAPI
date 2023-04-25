from pydantic import BaseModel
from typing import Optional
from fastapi import UploadFile, File


class User(BaseModel):
    # userId: int = 0
    name: str = ""
    email: str  = ""
    phone_no: str   = ""
    password: str   = ""
    # user_pic: Optional[bytes] = None
    # user_pic: Optional[UploadFile] = None

    # class Config:
    #     orm_mode = True
