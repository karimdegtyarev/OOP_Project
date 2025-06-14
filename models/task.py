from datetime import datetime
from typing import Optional
from pydantic import BaseModel, field_validator


class Task(BaseModel):
    id: Optional[int] = None
    title: str
    description: Optional[str] = None
    completed: bool = False
    due_date: Optional[datetime] = None
    project_id: Optional[int] = None
    user_id: Optional[int] = None


    @field_validator('title')
    @classmethod
    def title_must_not_be_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError('Title must not be empty')
        return v
