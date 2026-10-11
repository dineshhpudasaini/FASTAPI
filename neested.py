from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
class User(BaseModel):
    name:str
    age:int
    email:str

class Address(BaseModel):
    user:User
    address:str
    city:str

@app.post("/user")
def create_user(address:Address):
    return address