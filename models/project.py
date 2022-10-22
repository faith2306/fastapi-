from weakref import ref
from pydantic import BaseModel
from typing import Union

class Project(BaseModel):
    user: str
    title: str
    description: str
    team: str