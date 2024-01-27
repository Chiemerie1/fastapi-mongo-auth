from fastapi import FastAPI, Depends
import requests
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
from auth_mongo.schemas import UserDefault
from bcrypt import hashpw, gensalt
from auth_mongo.database import user_record





app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/")
async def root():
    return {"message": "This is the root of the app"}


@app.post("/api/create-user")
async def create_user(user: UserDefault):
    hashed_password = hashpw(user.password.encode("utf-8"), gensalt())
    user_info = {
        "_id": user._id,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "username": user.username,
        "email": user.email,
        "phone": user.email,
        "password": hashed_password.decode("utf-8"),
        "date": user.date
    }
    save_user = user_record.insert_one(user_info)
    return {"message": f"{user.username} has been created succefully"}



@app.get("/api/user/login")
async def login(token: Annotated[str, Depends(oauth2_scheme)]):
    return {
        "token": token
    }

