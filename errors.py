from fastapi import FastAPI , HTTPException , Request
from fastapi.responses import JSONResponse

app = FastAPI()

class usernotfoundexception(Exception):
    def __init__(self , name : str):
        self.name = name

@app.exception_handler(usernotfoundexception)
def user_not_found(request : Request, exc :usernotfoundexception):
    return JSONResponse(
        status_code=404,
        content={
            "status":"error",
            "message":f"User {exc.name} not found"
        }
    )

@app.get("/user/{name}")
def get_user(name:str):
    if name!="dinesh":
        raise usernotfoundexception(name)
    return{
        "name":name
    }



#@app.get("/user{userid}")
# def get_user( userid= int):
#     if userid != 1:
#         raise HTTPException(
#             status_code=404,
#             detail="Not Found"
#         )
#     return{
#         "message":'user Fetched',
#         "data":{
#             "id":1,
#             "Name":"Dinesh",
#             "age":19
#         }
#     }
