from typing import Optional
from pydantic import BaseModel, field_validator


class Project(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None

    @field_validator('name')
    @classmethod
    def name_must_not_be_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError('Project name must not be empty')
        return v
