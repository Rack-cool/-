from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def index():
    return {"msg": "hello world"}

@app.get("/user/me")
async def get_user_me():
    return {"user_id": "current_user me"}

@app.get("/user/{user_id}")
async def get_user(user_id: str):
    return {"user_id": user_id}

