import os
import sys

sys.path.append(os.path.abspath("../fastapi-postgresql-mapper-configuration"))

from app.db.base_class import Base
from app.models.User import User, user_table
from app.models.Address import Address, address_table
from app.entity.AddressEntity import  address_entity
from app.annotations.AddressAnnotationEntity import  AddressEntity
from app.entity.UserEntity import user_entity
from app.annotations.UserAnnotationEntity import UserEntity

