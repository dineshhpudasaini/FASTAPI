from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    Name : str
    Age : int
    Email :str

@app.post("/create_user")
def create_user(user:User):
    return{
        "message":"User Created",
        "data":user
    }