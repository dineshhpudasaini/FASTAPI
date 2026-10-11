from fastapi import FastAPI
app = FastAPI()
@app.post("/create_users")
def create_users(user:dict):
    return {
       "data": user
    }