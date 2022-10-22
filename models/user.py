from pydantic import BaseModel
from typing import Union

class User(BaseModel):
    binusianId: str
    name: str
    email: str
    major: str
    batch: str