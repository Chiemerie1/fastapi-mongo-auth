from fastapi import FastAPI, Depends
import requests
from auth_mongo import database, user_schema
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated




app = FastAPI()

oauth_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/")
async def root():
    return {"message": "This is the root of the app"}


@app.post("/website/create/user")
async def user(user: user_schema.UserDefault):
    return {"user": user}


@app.get("/website/user/login")
async def login(token: Annotated[str, Depends(oauth_scheme)]):
    return {
        "token": token
    }

