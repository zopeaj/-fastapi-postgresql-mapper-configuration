import os
import sys

sys.path.append(os.path.abspath("../fastapi-postgresql-mapper-configuration"))

from app.mappers.mapper_registrys import mapper_registry
from app.annotations.UserAnnotationEntity import *
from app.entity.UserEntity import user_entity

from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    Table
)
from sqlalchemy.orm import (
    relationship
)

address_entity = Table('addressentity', mapper_registry.metadata,
                Column('id', Integer, primary_key=True),
                Column('userentity_id', Integer, ForeignKey('userentity.id')),
                Column('email_address', String(50))
          )

mapper_registry.map_imperatively(UserEntity, user_entity, properties={
    'addreses': relationship(AddressEntity, backref="userentity", order_by=address_entity.c.id)
})

mapper_registry.map_imperatively(AddressEntity, address_entity)
