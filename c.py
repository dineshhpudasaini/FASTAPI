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

@app.put("/todos/{todo_id}")
def update_todos(todo_id: int, updated_todo : Todo):
 for index, todo in enumerate(Todos):
    if todo.id == todo_id:
        Todos[index] = updated_todo
        return {"message": "Todo updated"}
 return {
   "message":"Error Not Found"
 }

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id:int):
   for index , todo in enumerate(Todos):
     if todo.id == todo_id:
       Todos.pop(index)
       return {
         "message":"Todo Deleted"
         }
   return{
      "message":"Error todo not found"
    }
      