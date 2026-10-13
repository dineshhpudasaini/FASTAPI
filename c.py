from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
todos = []

class Todo(BaseModel):
    id : int
    Task :str
    status : bool

@app.post("/todos")
def post_todo(list:Todo):
   todos.append(list)
   return {
       "message":"Todo Added",
       "data":todos
   }