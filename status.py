from fastapi import FastAPI , status , HTTPException
app = FastAPI()

@app.post("/",status_code = status.HTTP_201_CREATED)
def create_user():
    return {
        "message":"User Created"
    }

@app.get("/user")
def get_user():
    return{
        "status":"Success",
        "Message":"Data Fetched",
        "data":{"name":"Dinesh",
                "age":19,
                "userId":"dinesh089"
                }
    }