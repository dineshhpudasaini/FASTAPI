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