from pydantic import BaseModel, field_validator, model_validator
from datetime import date, datetime
from enum import Enum
from fastapi import FastAPI

form_list = []
next_id = 1

class Field(str,Enum):
    MEDICAL = "medical"
    NON_MEDICAL = "non-medical"
    COMMERCE = "commerce"
    ARTS = "arts"

class CreateForm(BaseModel):
    name: str
    email: str
    date_of_birth: date
    password: str
    confirm_password: str
    field: Field

    @field_validator("date_of_birth")
    @classmethod
    def check_date(cls, v:date):
        if v  >= date.today():
            raise ValueError("Date of birth cant be today")
        return v
    
    @field_validator("password")
    @classmethod
    def check_len(cls, v: str):
        if len(v.strip()) < 8:
            raise ValueError("Password must be 8 characters")
        if not any(char.isdigit() for char in v.strip()):
            raise ValueError("Password must contain at least one digit")
        return v.strip()
        
    @model_validator(mode="after")
    def validate_password(self):
        if self.confirm_password != self.password:
            raise ValueError("The  two passwords dont match")
        return self

class ReturnForm(BaseModel):
    id: int
    name: str
    email: str
    date_of_birth: date
    field: Field
    joined_at: datetime
    class_assigned: bool

app = FastAPI(title = "MY SIGN UP FORM")

@app.get("/form")
def view_form():
    return form_list

@app.post("/form" , response_model=ReturnForm)
def enter_details(form: CreateForm):
    global form_list, next_id
    new_entry = {
        "id": next_id,
        **form.model_dump(),
        "joined_at": datetime.now(),
        "class_assigned": False
    }
    form_list.append(new_entry)
    next_id += 1
    return new_entry
