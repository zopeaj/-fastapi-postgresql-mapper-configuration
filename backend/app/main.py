import os
import sys

sys.path.append(os.path.abspath("../fastapi-postgresql-mapper-configuration/backend"))

from app.db.base import Base, user_entity, user_table, address_table, address_entity
from app.db.Session import engine
from app.db.mapper import mapper_registry


mapper_registry.metadata.create_all(engine)


# Runtime Introspection of Mapped classes and Mappers
from sqlalchemy import inspect

# user_entity_mapper = user_entity.__mapper__
# user_table_mapper = user_table.__mapper__


# address_entity_mapper = address_entity.__mapper__
# address_table_mapper = address_table.__mapper__

# user_entity_inspect_mapper = inspect(user_entity)
# user_table_inspect_mapper = inspect(user_table)

# address_entity_inspect_mapper = inspect(address_entity)
# address_table_inspect_mapper = inspect(address_table)

# user_tab = user_table.__table__
# user_tab = inspect(user_table).local_table


# selectables
user_tabs = inspect(user_table).selectable





