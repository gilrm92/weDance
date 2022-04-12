from typing import Optional
import uuid
from pydantic import BaseModel, Field

class Student(BaseModel):
    id: Optional[str] = str(uuid.uuid4())
    name: str
    age: int
    cpf: str
    email: str