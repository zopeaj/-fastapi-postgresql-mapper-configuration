import os
import sys

sys.path.append(os.path.abspath("../fastapi-postgresql-mapper-configuration"))

from app.db.base_class import Base
from app.models.User import User, user_table
from app.models.Address import Address, address_table

