from pydantic import BaseModel, EmailStr, constr
from typing import Optional


class UserCreate(BaseModel):
    username: constr(min_length=3, max_length=20)
    email: EmailStr
    full_name: Optional[constr(max_length=50)] = None


class UserUpdate(BaseModel):
    username: Optional[constr(min_length=3, max_length=20)] = None
    email: Optional[EmailStr] = None
    full_name: Optional[constr(max_length=50)] = None


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    full_name: Optional[str] = None

    class Config:
        from_attributes = True
