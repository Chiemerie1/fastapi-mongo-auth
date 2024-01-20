from fastapi import FastAPI, Depends
import requests
from auth_mongo import database, user_schema
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated




app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/")
async def root():
    return {"message": "This is the root of the app"}


@app.post("/api/create/user")
async def user(user: user_schema.UserDefault):
    return {"user": user}


@app.get("/api/user/login")
async def login(token: Annotated[str, Depends(oauth2_scheme)]):
    return {
        "token": token
    }

