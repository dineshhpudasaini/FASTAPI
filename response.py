from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name:str
    age:int
    password:str
 
class userResponse(BaseModel):
    name:str
    age:int

@app.get("/user",response_model=userResponse)
def get_user():
    return{
        "nama":"Dinesh",
        "age":19,
        "password":"123456"
    } 
