from fastapi import FastAPI
from pydantic import BaseModel

class userinfo(BaseModel):
    name:str
    userid:str
    Password:str

class response(BaseModel):
    name:str
    userid:str

app = FastAPI()

@app.get("/" , response_model=response)
def get_user():
    return{
        "name":"Dinesh",
        "userid":"dinesh089",
        "password":"Password089"
    }