from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message":"Hello From FastApi"}

@app.get("/users")
def get_users( name : str = None):
    return{
        "Name":name
    }
@app.get("/items")
def get_items(name : str =None , limit : int = 10):
    return {
        "item":name,
        "price":limit
    }