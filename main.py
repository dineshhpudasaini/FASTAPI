from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return{"message":"hello home"}

@app.get("/about")
def about():
    return {"message":"This is about page"}

@app.get("/users")
def users():
    return {
        "users":["Dinesh","Prahar","Ram","Gyalzen"]
            }