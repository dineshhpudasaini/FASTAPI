from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

todos = []

class Todo(BaseModel):
    id:int
    list:str
    completed:bool

@app.post("/todo")
def todo(list:Todo):
    todos.append(list)
    return{
        "message":"todo added", 
           "datas": list
           }

@app.get("/todo")
def todo():
    return todos

@app.get("/todo/{todo_id}")
def todo(todo_id:int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    return {"message":"to do not found"}

@app.put("/todos/{todo_id}")
def update_todo(todo_id : int , updated_todo: Todo):
    for index,todo in enumerate(todos):
        if todo.id == todo_id : 
            todos[index]=update_todo
            return{
        "message":"Data Updated",
        "data":updated_todo
        }
        return {"error":"To donot found"}