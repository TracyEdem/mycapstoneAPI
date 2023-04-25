from enum import Enum
from sqlalchemy import Enum as SQLAlchemyEnum,  Integer, String, Table, Column, Float, Date, ForeignKey
from config.db import meta, engine
from models.user import users 
from models.client import clients
from models.cut import cuts

class Status(Enum):
    COMPLETE = 'Complete'
    INCOMPLETE = 'Incomplete'

class Express(Enum):
    TRUE = 'True'
    FALSE = 'False'

projects = Table('projects',meta,
            Column('projectId',Integer, primary_key=True),
            Column('title', String(200), unique=True),
            Column('userId',Integer, ForeignKey(users.c.userId)), #foreign key
            Column('clientId',Integer, ForeignKey(clients.c.clientId)), #foreign key
            Column('cutId',Integer, ForeignKey(cuts.c.cutId)), #foreign key
            Column('description', String(200)),
            Column('descimg', String(255)),
            Column('fee', Float),
            Column('status',SQLAlchemyEnum(Status), default='Incomplete'),
            Column('isExpress',SQLAlchemyEnum(Express), default='False'),
            Column('due_date', Date),
              )

meta.create_all(engine)