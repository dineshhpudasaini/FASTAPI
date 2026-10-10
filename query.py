from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "FastAPI is working!"}

@app.get("/users")
def get_users(name:str=None):
    return{
        "Name":name
    }