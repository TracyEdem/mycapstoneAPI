from sqlalchemy import Integer,Table, Column, Float, ForeignKey
from config.db import meta, engine
from models.client import clients

measurements = Table('measurements',meta,
            Column('measurementId',Integer, primary_key=True),
            Column('bustCirc', Float),
            Column('waistCirc', Float),
            Column('accrossBack', Float),
            Column('biceps', Float),
            Column('sleeveLen', Float),
            Column('shoulderWaist', Float),
            Column('clientId',Integer, ForeignKey(clients.c.clientId)), #foreign key
            Column('nipNip', Float),
            Column('nipShoulder', Float),
            Column('dressLen', Float),
            Column('hipCirc', Float),
            Column('kneeCirc', Float),
            Column('skirtLen', Float),
            Column('thighWidth', Float),
            Column('trouserLen', Float),
            Column('waistKnee', Float),
            )

meta.create_all(engine)