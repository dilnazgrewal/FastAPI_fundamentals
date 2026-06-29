# Build a SignupForm model with password: str and confirm_password: str, using @model_validator(mode="after") to ensure they match, and a @field_validator on password enforcing it's at least 8 characters and contains at least one digit (use a small helper check, no regex required — though regex is fine if you prefer it).

from pydantic import BaseModel, field_validator, model_validator
from datetime import date
from enum import Enum
from fastapi import FastAPI

form_list = []

class Field(str,Enum):
    MEDICAL = "medical"
    NON_MEDICAL = "non-medical"
    COMMERCE = "commerce"
    ARTS = "arts"

class Form(BaseModel):
    name: str
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

app = FastAPI(title = "MY SIGN UP FORM")

@app.get("/form")
def view_form():
    return form_list

@app.post("/form")
def enter_details(form: Form):
    global form_list
    form_list.append(form)
    return form_list
