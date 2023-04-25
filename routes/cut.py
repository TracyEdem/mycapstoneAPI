from fastapi import APIRouter
from config.db import conn
from models.cut import cuts
from schemas.cut import Cut
from sqlalchemy import insert, select
from fastapi.encoders import jsonable_encoder


cut = APIRouter()

@cut.get('/get')
def fetch_cuts():
    res = conn.execute(select(cuts))
    rows = res.fetchall()
    cuts_list = [jsonable_encoder(Cut(**row._asdict())) for row in rows]
    return cuts_list


@cut.post('/post')
def post_cut(cut: Cut):
    try:
        conn.execute(cuts.insert().values(style=cut.style))
        conn.commit()
        return {"msg": "cut added successfully"}
    except Exception as e:
        conn.rollback()
        return {"msg": f"Error: {str(e)}"}


@cut.put('/update')
def update_cut(id: int, cut: Cut):
    try:
        conn.execute(cuts.update().values(style=cut.style).where(cuts.c.cutId == id))
        conn.commit()
        return {"msg": "cut updated successfully"}
    except Exception as e:
        conn.rollback()
        return {"msg": f"Error: {str(e)}"}

@cut.delete('/delete')
def delete_cut(id: int):
    try:
        conn.execute(cuts.delete().where(cuts.c.cutId == id))
        conn.commit()
        return {"msg": "cut deleted successfully"}
    except Exception as e:
        conn.rollback()
        return {"msg": f"Error: {str(e)}"}