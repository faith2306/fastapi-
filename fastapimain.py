import uuid
from enum import Enum

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List, Union
# from uuid import UUID, uuid4

# uncomment this if you want to get team names from a dictionary 

# class student_name(str, Enum):
#     misa = "misa xirinda M"
#     paul = "paul john U"
#     cate = "cate pico k"


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


# dummy database
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

# get request
@app.get("/general user/project/")
# async def view_project():
async def v_p():
    return db

# post request
@app.post("/student/project")
async def create_project(item: Project):
    db.append(item)
    return item

# put request
@app.put("/student/project/")
async def modify_project(title: str, item: Project):
    result = {"title": title, **item.dict()}
    if item:
        result.update({"item": item})
    return result
    return {"title": title, "project_id": project_id}

# delete request
@app.delete("/student/project/")
async def d_u(p_id: int):
    for project in db:
        if project.project_id == p_id:
            db.remove(project)
            return
