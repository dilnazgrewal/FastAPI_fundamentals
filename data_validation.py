from pydantic import BaseModel, field_validator, model_validator
from datetime import date

class TaskCreate(BaseModel):
    title: str
    start_date: date
    due_date: date

    @field_validator("title")
    @classmethod
    def title_not_blank(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("title cannot be blank or whitespace")
        return v.strip()

    @model_validator(mode="after")
    def due_after_start(self):
        if self.due_date < self.start_date:
            raise ValueError("due_date must be after start_date")
        return self