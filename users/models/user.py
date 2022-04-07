from typing import Optional
import uuid
from pydantic import BaseModel, Field


class User(BaseModel):
    id: Optional[str] = str(uuid.uuid4())
    name: str
    login: str
    password: str
