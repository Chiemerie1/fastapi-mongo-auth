from fastapi import FastAPI
import requests



app = FastAPI()

@app.get("/")
async def root():

    return {"message": "This is the root of the app"}


@app.get("/auth")
async def user():
    
    return {"Message": "the auth will go here"}