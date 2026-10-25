from fastapi import FastAPI , Depends

app = FastAPI()

def Common_logic():
    return{
        "user":"Dinesh"
    }

@app.get("/profile")
def profile(user = Depends(Common_logic)):
    return user
@app.get("/dashboard")
def profile(user = Depends(Common_logic)):
    return user