from fastapi import FastAPI , status , HTTPException
app = FastAPI()

@app.post("/",status_code = status.HTTP_201_CREATED)
def create_user():
    return {
        "message":"User Created"
    }

@app.get("/users")
def get_users():
    return{
        "status":"Success",
        "Message":"Data Fetched",
        "data":{"name":"Dinesh",
                "age":19,
                "userId":"dinesh089"
                }
    }

@app.get("/users{user_id}")
def get_user(userid : int):
    if userid != 1:
        raise HTTPException(
            status_code=404,
            detail="not Found"
        )
    return {
        "id":1,
        "name":"Dinesh"
    }