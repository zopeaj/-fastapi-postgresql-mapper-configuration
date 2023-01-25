from __future__ import annotations
from dataclasses import dataclass, field
import os
import sys

sys.path.append(os.path.abspath("../fastapi-postgresql-mapper-configuration"))


@dataclass
class AddressEntity:
    id: int = field(init=False)
    userentity_id: int = field(init=False)
    email_address: str = None
