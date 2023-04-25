from fastapi import APIRouter
from config.db import conn
from models.client import clients
from schemas.client import Client
from sqlalchemy import insert, select
from fastapi.encoders import jsonable_encoder


client = APIRouter()

@client.get('/get-client')
def fetch_clients( userid: int):
    res = conn.execute(select(clients).where(clients.c.userId == userid))
    rows = res.fetchall()
    print(rows)
    clients_list = [jsonable_encoder(Client(**row._asdict())) for row in rows]
    return clients_list


@client.post('/post-client')
def post_client(client: Client, userid: int ):
    try:
        conn.execute(clients.insert().values(name=client.name, phone_no=client.phone_no, gender=client.gender, balance=client.balance, userId=userid))
        conn.commit()
        return {"msg": "client added successfully"}
    except Exception as e:
        conn.rollback()
        return {"msg": f"Error: {str(e)}"}


@client.put('/update-client')
def update_client(userid: int, client: Client, clientid: int):
    try:
        conn.execute(clients.update().values(name=client.name, phone_no=client.phone_no, gender=client.gender, balance=client.balance).where(clients.c.userId == userid and clients.c.clientId == clientid))
        conn.commit()
        return {"msg": "client updated successfully"}
    except Exception as e:
        conn.rollback()
        return {"msg": f"Error: {str(e)}"}

@client.delete('/delete-client')
def delete_client(userid: int, clientid: int):
    try:
        conn.execute(clients.delete().where(clients.c.userId == userid and clients.c.clientId == clientid))
        conn.commit()
        return {"msg": "client deleted successfully"}
    except Exception as e:
        conn.rollback()
        return {"msg": f"Error: {str(e)}"}