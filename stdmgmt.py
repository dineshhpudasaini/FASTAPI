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

@app.get("/lists")
def get_students():
    return{
        "data":students
    }

@app.put("/lists/{students_id}")
def update_students(students_id : int, updated_students:Students):
    for index, lists in enumerate(students):
        if lists.Id == students_id:
            students[index]=updated_students
            return{
                "message":"Done"
            }
    return{
        "error":"Not Found"
    }

@app.delete("/lists/{students_id}")
def delete_students(students_id:int):
    for index , lists in enumerate(students):
        if lists.Id == students_id:
            students.pop(index)
            return{
                "message":"Deleted",
                "data":students
             }
    return{
        "error":"Data Not Found"
    }