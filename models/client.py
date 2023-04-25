from enum import Enum
from sqlalchemy import Enum as SQLAlchemyEnum, Integer, String, Table, Column, Float, ForeignKey
from config.db import meta, engine
from models.user import users
from sqlalchemy.orm import relationship

class Gender(Enum):
    MALE = 'Male'
    FEMALE = 'Female'

clients = Table('clients', meta,
            Column('clientId',Integer, primary_key=True),
            Column('name',String(100)),
            Column('phone_no', String(15)),
            Column('gender', SQLAlchemyEnum(Gender), default=Gender.FEMALE.value),
            Column('balance', Float),
            Column('userId',Integer, ForeignKey(users.c.userId)),
            # project = relationship(projects, backref='client'),
            # measurement = relationship(measurements, backref='client')
              )

meta.create_all(engine)