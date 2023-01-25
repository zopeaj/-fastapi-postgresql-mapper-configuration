from __future__ import annotations
import os
import sys

sys.path.append(os.path.abspath("../fastapi-postgresql-mapper-configuration"))
from app.db.mapper import mapper_registry

from sqlalchemy import (
    Column,
    Integer,
    String,
    Table
)


user_entity = Table('userentity', mapper_registry.metadata,
                    Column('id', Integer, primary_key=True),
                    Column('name', String(50)),
                    Column('fullname', String(50)),
                    Column('nickname', String(12)),
              )
