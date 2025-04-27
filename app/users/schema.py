from pydantic import BaseModel
from typing import Optional
# --- Models ---

class UserCreate(BaseModel):
    email: str
    password: str
    role: str

class UserUpdate(BaseModel):
    email: Optional[str] = None
    password: Optional[str] = None
    role: Optional[str] = None


class LoginRequest(BaseModel):
    email: str
    password: str

class TokenResponse(BaseModel):
    access_token: str

