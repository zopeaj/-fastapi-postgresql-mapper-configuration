import os
import sys

sys.path.append(os.path.abspath("../fastapi-postgresql-mapper-configuration"))

from sqlalchemy import Table, Integer, Column, String, ForeignKey
from sqlalchemy import MetaData
from app.mappers.mapper_registrys import mapper_registry
from app.models.User import User, user_table
from sqlalchemy.orm import relationship


address_table = Table(
                   'address', mapper_registry.metadata,
                    Column('id', Integer, primary_key=True),
                    Column('user_id', Integer, ForeignKey('user.id')),
                    Column('email_address', String(50))
            )

class Address:
    pass

mapper_registry.map_imperatively(User, user_table, properties={
    'addresses': relationship(Address, backref="user", order_by=address_table.c.id)
})

mapper_registry.map_imperatively(Address, address_table)
