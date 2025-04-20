from pydantic import BaseModel
from typing import Optional

class StudentSchema(BaseModel):
    name: str
    age: int
    grade: str

class UpdateStudentSchema(BaseModel):
    name: Optional[str]
    age: Optional[int]
    grade: Optional[str]
