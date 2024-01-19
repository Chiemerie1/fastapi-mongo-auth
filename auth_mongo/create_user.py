from pydantic import BaseModel



class User(BaseModel):
    username: str
    first_name: str
    last_name: str
    phone: str
    password: str
    confirm_password: str

    