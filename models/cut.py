from sqlalchemy import Integer, String, Table, Column, Float
from config.db import meta, engine
from sqlalchemy.orm import relationship


cuts = Table('cuts',meta,
            Column('cutId',Integer, primary_key=True),
            Column('style',String(30)),
            # catalog = relationship(catalogs, backref='cut')
              )

meta.create_all(engine)