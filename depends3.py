from fastapi import FastAPI , Depends , HTTPException , Header

app = FastAPI()

def verify_token(token : str = Header(None)):
    if token != "mysecrettoken":
        raise HTTPException(
            status_code=401,
            detail="unauthorized"

        )
    return{
        "user":"Authorised User"
    }
@app.get("/data")
def secure_data(user = Depends(verify_token)):
    return{
        "message":"Secure Data accessed",
        "user":user
    }