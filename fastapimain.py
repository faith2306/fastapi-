from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel
from enum import Enum
from typing import Optional, List, Union
from uuid import UUID, uuid4

from routes.user import user
from routes.project import project


# uncomment this if you want to get team names from a dictionary 
# class student_name(str, Enum):
#     misa = "misa xirinda M"
#     paul = "paul john U"
#     cate = "cate pico k"


# class Project(BaseModel):
#     project_id: Union[float, None] = None
#     title: str
#     description: str
#     team: str

# dummy database
# db: List[Project] = [
#     Project(
#         project_id=44,
#         title="brain box",
#         description="To store and display students project",
#         youtube="https://youtu.be/GN6ICac3OXY",
#         #team=student_name.misa, dont forget to change this back
#         team=student_name.misa,
#     ),

#     Project(
#         title="Gubugklakah SRS",
#         description="Get recommendations on services to "
#                     "provide during a vacation season ",
#         youtube="https://youtu.be/GN6ICac3OXY",
#         image="villageLandscape.png",
#         team=student_name.paul,
#     )
# ]

app = FastAPI(
    title='Project service',
    description='Project service using fastapi'
    )
app.include_router(user)
app.include_router(project)



# get request
# @app.get("/general user/project/")
# # async def view_project():
# async def v_p():
#     return db

# post request
# @app.post("/student/project")
# async def create_project(item: Project):
#     db.append(item)
#     return item


# delete request
# @app.delete("/student/project/")
# async def d_u(p_id: int):
#     for project in db:
#         if project.project_id == p_id:
#             db.remove(project)
#             return

