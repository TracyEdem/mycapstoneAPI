from fastapi import APIRouter,File, UploadFile
from config.db import conn
from models.project import projects
from schemas.project import Project
from models.project import Status, Express
from sqlalchemy import select, func
from fastapi.encoders import jsonable_encoder
import base64
from datetime import date


project = APIRouter()

@project.get('/get')
def fetch_projects():
    res = conn.execute(select(projects))
    rows = res.fetchall()
    projects_list = [jsonable_encoder(Project(**row._asdict())) for row in rows]
    return projects_list

@project.get('/get-pending')
def fetch_projects():
    query = select(
    func.count().label('incomplete_count')
).where(projects.c.status == Status.INCOMPLETE.value)

    res= conn.execute(query)
    rows = res.fetchall()
    total =rows[0][0]

    return total
    
@project.get('/get-complete')
def fetch_projects():
    query = select(
    func.count().label('complete_count')
).where(projects.c.status == Status.COMPLETE.value)

    res= conn.execute(query)
    rows = res.fetchall()
    total =rows[0][0]

    return total


@project.get('/get-express')
def fetch_projects():
    query = select(
    func.count().label('express_count')
).where(projects.c.isExpress == Express.TRUE.value)

    res= conn.execute(query)
    rows = res.fetchall()
    total =rows[0][0]
    return total

@project.post('/post')
def post_project(project: Project):
    try:
        conn.execute(projects.insert().values(title=project.title, userId=project.userId, clientId=project.clientId, 
                                            cutId=project.cutId, description=project.description,
                                            fee=project.fee, status=project.status, isExpress=project.isExpress, due_date=project.due_date))
        conn.commit()
        return {"msg": "project added successfully"}
    except Exception as e:
        conn.rollback()
        return {"msg": f"Error: {str(e)}"}


@project.put('/update/{id}')
def update_project(id: int, project: Project):
    try:
        conn.execute(projects.update().values(title=project.title, userId=project.userId, clientId=project.clientId, 
                                            cutId=project.cutId, description=project.description, 
                                            fee=project.fee, status=project.status, isExpress=project.isExpress, due_date=project.due_date).where(projects.c.projectId == id))
        conn.commit()
        return {"msg": "project updated successfully"}
    except Exception as e:
        conn.rollback()
        return {"msg": f"Error: {str(e)}"}
    
@project.put('/update-descimg/{id}')
async def update_img(id: int, file: UploadFile = File(None)):
    
    try:
        if file:
            file_contents = await file.read()
            file_encoded = base64.b64encode(file_contents)
        else:
            file_encoded = None
        print(id)
        conn.execute(projects.update().values(image=file_encoded).where(projects.c.projectId == id))
        conn.commit()
        print("got here")
        return {"msg": "descriptive image updated successfully"}
    except Exception as e:
        return {"msg": f"Error: {str(e)}"}

@project.delete('/delete/{id}')
def delete_project(id: int):
    try:
        conn.execute(projects.delete().where(projects.c.projectId == id))
        conn.commit()
        return {"msg": "project deleted successfully"}
    except Exception as e:
        conn.rollback()
        return {"msg": f"Error: {str(e)}"}