from fastapi import FastAPI
import requests
from auth_mongo import database, user_schema



app = FastAPI()

@app.get("/")
async def root():
    return {"message": "This is the root of the app"}


@app.post("/website/user")
async def user(user: user_schema.UserDefault):
    return {"user": user}

