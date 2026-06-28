from pydantic import BaseModel
from fastapi import FastAPI

class Student(BaseModel):
    name: str
    marks: float
    urn: int
    passed: bool

students = [
    Student(name="Dilnaz", marks=92.5, urn=101, passed=True),
    Student(name="Rahul", marks=85.0, urn=102, passed=True),
    Student(name="Priya", marks=38.5, urn=103, passed=False),
]

app = FastAPI(title="Students Record")

@app.get("/record")
def list_students():
    return students

@app.post("/record")
def add_student(student:Student):
    students.append(student)
    print(f"{student.urn} added successfully")



