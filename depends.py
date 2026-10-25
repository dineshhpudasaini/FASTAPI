from fastapi import FastAPI , Depends

app=FastAPI()

def common_logic():
    return {
        "message":"Common Logic Executed"
    }

@app.get("/home")
def home(data = Depends(common_logic)):
    return data