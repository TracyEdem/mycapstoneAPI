from fastapi import APIRouter,File, UploadFile, Form, Depends
from config.db import conn
from models.user import users
from schemas.user import User
from sqlalchemy import insert, select
from fastapi.encoders import jsonable_encoder
import base64


user = APIRouter()
trans = conn.begin()

@user.get('/get-user')
def fetch_users(id: int):
    res = conn.execute(select(users).where(users.c.userId == id))
    rows = res.fetchall()
    users_list = [jsonable_encoder(User(**row._asdict())) for row in rows]
    return users_list

@user.post('/login')
def login(user : User):
    print(user)
    res = conn.execute(select(users).where(users.c.name == user.name and  users.c.email == user.email and users.c.password == user.password))
    rows = res.fetchall()

    if rows:
        return rows[0][0]
    else:
        return {"Error"}


@user.post('/post-user')
async def post_user(user: User):
    try:
        conn.execute(users.insert().values(name=user.name, email=user.email, phone_no=user.phone_no, password=user.password))
        conn.commit()
        return {"msg": "user added successfully"}
    except Exception as e:
        conn.rollback()
        return {"msg": f"Error: {str(e)}"}
   

@user.put('/update-user/{id}')
def update_user(id: int, user: User):
    try:
        conn.execute(users.update().values(email=user.email, phone_no=user.phone_no, password=user.password).where(users.c.userId == id))
        conn.commit()
        return {"msg": "user updated successfully"}
    except Exception as e:
        conn.rollback()
        return {"msg": f"Error: {str(e)}"}

@user.put('/update-profilepic/{id}')
async def update_pic(id: int, file: UploadFile = File(None)):
    
    try:
        if file:
            file_contents = await file.read()
            file_encoded = base64.b64encode(file_contents)#.decode("utf-8")
        else:
            file_encoded = None
        print(id)
        conn.execute(users.update().values(user_pic=file_encoded).where(users.c.userId == id))
        conn.commit()
        print("got here")
        return {"msg": "profile picture updated successfully"}
    except Exception as e:
        return {"msg": f"Error: {str(e)}"}
    
   
    
@user.delete('/delete-user/{id}')
def delete_user(id: int):
    try:
        conn.execute(users.delete().where(users.c.userId == id))
        conn.commit()
        return {"msg": "user deleted successfully"}
    except Exception as e:
        conn.rollback()
        return {"msg": f"Error: {str(e)}"}

