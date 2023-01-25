from __future__ import annotations
from dataclasses import dataclass, field
import os
import sys

sys.path.append(os.path.abspath("../fastapi-postgresql-mapper-configuration"))

from app.annotations.AddressAnnotationEntity import AddressEntity
from typing import List


@dataclass
class UserEntity:
    id: int = field(init=False)
    name: str = None
    fullname: str = None
    nickname: str = None
    addresses: List[AddressEntity] = field(default_factory=list)
