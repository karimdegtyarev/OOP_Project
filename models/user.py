from pydantic import BaseModel, EmailStr, constr, field_validator
from typing import Optional


class User(BaseModel):
    id: Optional[int] = None
    username: constr(min_length=3, max_length=20)  # Ограничение длины
    email: EmailStr  # Автоматическая валидация email
    full_name: Optional[constr(max_length=50)] = None  # Ограничение длины

    @field_validator('username')
    @classmethod
    def username_alphanumeric(cls, v: str) -> str:
        if not v.isalnum():
            raise ValueError('Имя пользователя должно содержать только буквы и цифры')
        return v

    @field_validator('full_name')
    @classmethod
    def full_name_no_special_chars(cls, v: Optional[str]) -> Optional[str]:
        if v and not all(c.isalpha() or c.isspace() for c in v):
            raise ValueError('ФИО должно содержать только буквы и пробелы')
        return v
