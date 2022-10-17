import uuid
from enum import Enum

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List, Union
from uuid import UUID, uuid4




class student_name(str, Enum):
    misa = "misa xirinda M"
    paul = "paul john U"
    cate = "cate milo k"


class Project(BaseModel):
    project_id: int  # Optional[uuid] = uuid4
    title: str
    description: str
    youtube: Optional[str]
    image: Optional[str]
    team: List[student_name]

app = FastAPI(
    title='Brain Box',
    description='Bla description'
    )

db: List[Project] = [
    Project(
        project_id=44,
        title="brain box",
        description="To store and display students project",
        youtube="https://youtu.be/GN6ICac3OXY",
        team=student_name.misa,
    ),

    Project(
        title="Gubugklakah SRS",
        description="Get recommendations on services to "
                    "\n provide during a vacation season ",
        youtube="https://youtu.be/GN6ICac3OXY",
        image="villageLandscape.png",
        team=student_name.paul,
    )
]


# class Item(BaseModel):
#     id: Optional[uuid] = uuid4
#     title: str
#     description: str
#     youtube: Optional[str]
#     image: str
#     team: str


@app.get("/")
async def view_project():
    # return {"project_id": "acvdsdas12321", "title": "Random Title"}
    return db

#
# @app.post("/")
# async def create_project(project: Project):
#     # item_dict = item.dict()
#     # if item.tax:
#     #     price_with_tax = item.price + item.tax
#     #     item_dict.update({"price_with_tax": price_with_tax})
#     # return item_dict
#     db.append(project)
#     return {"id": Project.project_id}
#
#
# # @app.put("/modify/{b_id}")
# # async def modify_project(id: int, item: Item):
async def modify_project(item_id: int, item: Item, q: Union[str, None] = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result
    return {"item_name": item.name, "item_id": item_id}
#
#
# @app.delete("/delete/{p_id}")
# async def delete_user(p_id: UUID):
#     for project in db:
#         if project.project_id == p_id:
#             db.remove(project)
#             return
#
#         # title = "brain box",
#         # description = "To store and display students project",
#         # youtube = "https://youtu.be/GN6ICac3OXY",
#         # team = student_name.misa,
