from fastapi import FastAPI

app = FastAPI()

# Basic Home Page
@app.get("/")
def home():
    return {"message": "FastAPI is working!"}

# no value for no user
@app.get("/users")
def get_users(name:str=None):
    return{
        "Name":name
    }
# DEfault limit
@app.get('/products')
def get_products(limit:int=10):
    return{
        "Limit":limit
    }

# multiple datas
@app.get("/items")
def get_items(name: str=None, price :int=0):
    return{
        "name":name,
        "price":price
    }