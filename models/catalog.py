from sqlalchemy import Integer, String, Table, Column, ForeignKey
from config.db import meta, engine
from models.cut import cuts
from models.user import users



catalogs = Table('catalogs',meta,
            Column('catalogId',Integer, primary_key=True),
            Column('cutId',Integer, ForeignKey(cuts.c.cutId)), #foreign key
            Column('descriptor', String(200)),
            Column('image', String(255)),
            Column('userId',Integer, ForeignKey(users.c.userId)), #foreign key
              )

meta.create_all(engine)

