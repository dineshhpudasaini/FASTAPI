from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

Todos = []

class Todo(BaseModel):
 id:int
 task : str
 status:bool

@app.post("/todos")
def post_todo(list:Todo):
 Todos.append(list)
 return {
  "message":"Todo added",
  "data":Todos
 }

@app.get("/todos")
def get_todos():
 return{
  "datas":Todos
 }

@app.put("/todos{todo_id}")
def update_todos(todo_id: int):
 return {"message": "Updated", "id": todo_id}