from sqlalchemy import Integer, String, Table, Column, LargeBinary
from config.db import meta, engine
from sqlalchemy.orm import relationship



users = Table('users',meta,
            Column('userId',Integer, primary_key=True),
            Column('name', String(12), unique=True),
            Column('email', String(50), unique=True,),
            Column('phone_no', String(15)),
            Column('password', String(20)),
            Column('user_pic', LargeBinary),
              )

meta.create_all(engine)

