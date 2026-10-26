from fastapi import FastAPI, Request

app = FastAPI()

@app.middleware("https")
async def my_middleware(request:Request , call_next):
    