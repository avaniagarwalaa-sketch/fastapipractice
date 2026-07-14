from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
app = FastAPI()
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/avani/hell")
def check(age: int):
    return {"age": f"{age} is here"}

@app.get("/avani/{name}")
def read(name: str):
    return {"hello": f"{name} is here"}

@app.get("/k")
def readk(name: Optional[str] = "avani"):
    return {"mssg":f"{name}"}

class Student(BaseModel):
    name: str
    age: int
    roll: int

@app.post("/create_student")
def createstudent(student: Student):
    return {
        "name":student.name,
        "age":student.age,
        "roll":student.roll
    }
