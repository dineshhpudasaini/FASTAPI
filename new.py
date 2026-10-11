from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name:str
    age:int


@app.post("/create_users")
def create_users(user:User):
    return {
       "data": user
    }