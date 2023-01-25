import os
import sys

sys.path.append(os.path.abspath("../fastapi-postgresql-mapper-configuration/backend"))

from app.db.base import Base, user_entity, user_table, address_table, address_entity
from app.db.Session import engine
from app.db.mapper import mapper_registry


mapper_registry.metadata.create_all(engine)







