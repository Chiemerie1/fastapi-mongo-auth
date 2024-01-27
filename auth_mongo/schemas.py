from pydantic import BaseModel
import random
import string
import random
from datetime import datetime
from fastapi import Form




def code():
    code = random.choices(string.ascii_letters + string.digits, k=6)
    return "".join(code)


class UserDefault(BaseModel):
    _id: str = code()
    first_name: str = Form()
    last_name: str = Form()
    username: str = Form()
    email: str = Form()
    phone: str = Form()
    password: str = Form()
    date: datetime
        
    class Config:
        from_attributes = True
    

# class UserPassword(UserDefault):
#     password: str
#     confirm_password: str | None
    
#     def password_check(cls):
#         if len(cls.password) != len(cls.confirm_password):
#             raise  ValueError("Both passwords are not the same length")
#         elif cls.password != cls.confirm_password:
#             raise ValueError("both passwords must be the same")
#         return cls.password
    
    

class UserPermission(UserDefault):
    is_active: bool = False
    is_superuser: bool = False
    is_admin: bool = False
    
    class Config:
        orm_mode = True



class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


        

        

# class Config:
#     orm_mode = True
#     allow_population_by_field_name = True
#     arbitrary_types_allowed = True


# @validator("high_risk_period_end")
# def handle_high_risk_periods(cls, v, values, **kwargs):
#     if "high_risk_period_start" in values and v == values["high_risk_period_start"]:
#         raise ValueError("The high_risk_period_start and high_risk_period_end cannot be the same")
#     return v