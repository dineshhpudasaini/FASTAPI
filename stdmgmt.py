from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
students = []
class Students(BaseModel):
    Id : int
    Name : str
    Grade : str
    Course : str
    free : bool

@app.post("/lists")
def post_students(list : Students):
    students.append(list)
    return{
        "message":"studente Added",
        "data":students
    }