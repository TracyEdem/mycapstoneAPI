from fastapi import APIRouter
from config.db import conn
from models.measurement import measurements
from schemas.measurement import Measurement
from sqlalchemy import select
from fastapi.encoders import jsonable_encoder

measurement = APIRouter()

@measurement.get('/get')
def fetch_measurements(clientid: int):
    res = conn.execute(select(measurements).where(measurements.c.clientId == clientid))
    rows = res.fetchall()
    measurements_list = [jsonable_encoder(Measurement(**row._asdict())) for row in rows]
    # print(measurements_list)
    return measurements_list



@measurement.post('/post')
def post_measurement(measurement: Measurement, clientid: int):
    try:
        conn.execute(measurements.insert().values(bustCirc=measurement.bustCirc, waistCirc=measurement.waistCirc, accrossBack=measurement.accrossBack, 
                                                     biceps=measurement.biceps, sleeveLen=measurement.sleeveLen, shoulderWaist=measurement.shoulderWaist,
                                                     clientId=clientid,nipNip=measurement.nipNip,nipShoulder=measurement.nipShoulder,
                                                     dressLen=measurement.dressLen,hipCirc=measurement.hipCirc, kneeCirc=measurement. kneeCirc,
                                                     skirtLen=measurement.skirtLen,thighWidth=measurement.thighWidth,trouserLen=measurement.trouserLen,
                                                     waistKnee=measurement.waistKnee))
        conn.commit()
        return {"msg": "measurements added successfully"}
    except Exception as e:
        conn.rollback()
        return {"msg": f"Error: {str(e)}"}

@measurement.put('/update')
def update_measurement(clientid: int, measurement: Measurement):
    try:
        conn.execute(measurements.update().values(bustCirc=measurement.bustCirc, waistCirc=measurement.waistCirc, accrossBack=measurement.accrossBack, 
                                                     biceps=measurement.biceps, sleeveLen=measurement.sleeveLen, shoulderWaist=measurement.shoulderWaist,
                                                     nipNip=measurement.nipNip,nipShoulder=measurement.nipShoulder,
                                                     dressLen=measurement.dressLen,hipCirc=measurement.hipCirc, kneeCirc=measurement. kneeCirc,
                                                     skirtLen=measurement.skirtLen,thighWidth=measurement.thighWidth,trouserLen=measurement.trouserLen,
                                                     waistKnee=measurement.waistKnee).where(measurements.c.clientId == clientid))
        conn.commit()
        return {"msg": "measurements updated successfully"}
    except Exception as e:
        conn.rollback()
        return {"msg": f"Error: {str(e)}"}

@measurement.delete('/delete')
def delete_measurement(clientid: int):
    try:
        conn.execute(measurements.delete().where(measurements.c.clientId == clientid))
        conn.commit()
        return {"msg": "measurements deleted successfully"}
    except Exception as e:
        conn.rollback()
        return {"msg": f"Error: {str(e)}"}