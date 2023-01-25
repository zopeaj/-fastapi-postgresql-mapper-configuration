import os
import sys

sys.path.append(os.path.abspath("../fastapi-postgresql-mapper-configuration"))


from __future__ import annotations
from dastaclasses import dataclass, field
from typing import List
from app.entity.AddressEntity import AddressEntity


from sqlalchemy import (
    Column,
    Integer,
    String,
    Table
)
from sqlalchemy.orm import (
    relationship
)


@dataclass
class UserEntity:
    id: int = field(init=False)
    name: str = None
    fullname: str = None
    nickname: str = None
    addresses: List[AddressEntity] = field(default_factory=list)


user_entity = Table('userentity', mapper_registry.metadata,
                    Column('id', Integer, primary_key=True),
                    Column('name', String(50)),
                    Column('fullname', String(50)),
                    Column('nickname', String(12)),
              )
