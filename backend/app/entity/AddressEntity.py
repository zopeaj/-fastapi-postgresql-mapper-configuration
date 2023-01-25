from __future__ import annotations
from dastaclasses import dataclass, field
from typing import List
from app.mappers.mapper_registrys import mapper_registry
from app.entity.UserEntity import UserEntity, user_entity


from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    MetaData,
    String,
    Table
)
from sqlalchemy.orm import (
    relationship
)

@dataclass
class AddressEntity:
    id: int = field(init=False)
    userentity_id: int = field(init=False)
    email_address: str = None

address_entity = Table('addressentity', mapper_registry.metadata,
                Column('id', Integer, primary_key=True),
                Column('userentity_id', Integer, ForeignKey('userentity.id')),
                Column('email_address', String(50))
          )

mapper_registry.map_imperatively(UserEntity, user_entity, properties={
    'addreses': relationship(AddressEntity, backref="userentity", order_by=address_entity.c.id)
})

mapper_registry.map_imperatively(AddressEntity, address_entity)
