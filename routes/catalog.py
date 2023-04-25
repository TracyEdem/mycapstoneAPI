import io
from fastapi import APIRouter,File, UploadFile
from config.db import conn
from models.catalog import catalogs
from schemas.catalog import Catalog
from sqlalchemy import insert, select
from fastapi.encoders import jsonable_encoder
import base64
from fastapi.responses import FileResponse, StreamingResponse

catalog = APIRouter()

@catalog.get('/get')
def fetch_catalogs():
    res = conn.execute(select(catalogs))
    rows = res.fetchall()
    catalogs_list = [jsonable_encoder(Catalog(**row._asdict())) for row in rows]
    return catalogs_list

@catalog.get('/get-img')
def fetch_catalogs():
    res = conn.execute(select(catalogs))
    rows = res.fetchall()
    images = []
    for row in rows:
        image_bytes = base64.b64decode(row[3])
        image_path = f"{row[0]}.jpg"
        with open(image_path, "wb") as f:
            f.write(image_bytes)
        images.append({"catalog_id": row[0], "image_path": image_path})
    return {"images": images}




@catalog.post('/post')
def post_catalog(catalog: Catalog, userid: int):
    try:
        conn.execute(catalogs.insert().values(cutId=catalog.cutId, descriptor=catalog.descriptor, userId=userid))
        conn.commit()
        return {"msg": "item added successfully"}
    except Exception as e:
        conn.rollback()
        return {"msg": f"Error: {str(e)}"}
    

@catalog.put('/update-img')
async def update_img(userid: int, catalogid: int,file: UploadFile = File(None)):
    
    try:
        if file:
            file_contents = await file.read()
            file_encoded = base64.b64encode(file_contents)
        else:
            file_encoded = None
        print(id)
        conn.execute(catalogs.update().values(image=file_encoded).where(catalogs.c.userId == userid and catalogs.c.catalogId == catalogid))
        conn.commit()
        return {"msg": "catalog image updated successfully"}
    except Exception as e:
        conn.rollback()
        return {"msg": f"Error: {str(e)}"}


@catalog.put('/update')
def update_catalog(userid: int, catalogid: int,catalog: Catalog):
    try:
        conn.execute(catalogs.update().values(cutId=catalog.cutId, descriptor=catalog.descriptor).where(catalogs.c.userId == userid and catalogs.c.catalogId == catalogid ))
        conn.commit()
        return {"msg": "catalog updated successfully"}
    except Exception as e:
        conn.rollback()
        return {"msg": f"Error: {str(e)}"}

@catalog.delete('/delete')
def delete_catalog(userid: int, catalogid: int):
    try:
        conn.execute(catalogs.delete().where(catalogs.c.userId == userid and catalogs.c.catalogId == catalogid))
        conn.commit()
        return {"msg": "item deleted successfully"}
    except Exception as e:
        conn.rollback()
        return {"msg": f"Error: {str(e)}"}




