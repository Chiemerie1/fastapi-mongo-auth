from pydantic import BaseModel
from datetime import datetime



class User(BaseModel):
    username: str
    first_name: str
    last_name: str
    phone: str
    password: str
    confirm_password: str
    date : datetime

    