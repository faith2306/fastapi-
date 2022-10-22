from fastapi import APIRouter
from models.project import Project
from config.db import conn
from schemas.project import projectEntity, projectsEntity
from bson import ObjectId


project = APIRouter()

# GET ALL PROJECTS
@project.get('/project')
async def get_all_projects():    
    return projectsEntity(conn.local.project.find())

# GET PROJECT BY ID
@project.get('/project/{id}')
async def find_one_project(id):
    return projectEntity(conn.local.project.find_one({"_id": ObjectId(id)}))

# INSERT PROJECT
@project.post('/project')
async def create_project(project: Project):
    conn.local.project.insert_one(dict(project))
    return projectsEntity(conn.local.project.find())

# UPDATE PROJECT BY ID
@project.put('/project/{id}')
async def update_project(id, project: Project):
    conn.local.project.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": dict(project)
    })
    return projectEntity(conn.local.project.find_one({"_id": ObjectId(id)}))

#  DELETE PROJECT BY ID
@project.delete('/project/{id}')
async def delete_project(id):
    return projectEntity(conn.local.project.find_one_and_delete({"_id": ObjectId(id)}))