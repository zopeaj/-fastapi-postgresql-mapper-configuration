import os
import sys

sys.path.append(os.path.abspath("../fastapi-postgresql-mapper-configuration"))

from sqlalchemy import Table, Column, String, Integer
from sqlalchemy import MetaData
from app.mappers.mapper_registrys import mapper_registry

user_table = Table(
                   'user',
                    mapper_registry.metadata,
                    Column('id', Integer, primary_key=True),
                    Column('name', String(50)),
                    Column('fullname', String(50)),
                    Column('age', Integer),
                    Column('nickname', String(12))
            )
class User:
    pass

