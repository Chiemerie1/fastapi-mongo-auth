from datetime import datetime, timedelta, timezone
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel



SECRET_KEY = "f36457af3e25696b50a1abae3bbf65e2e529f3a6cff5619ceb4f75650ef0b426"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRATION_MINUTES = 30


password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def hash_password(password):
    return password_context.hash(password)


def check_password(password, hashed_password):
    return password_context.verify(password, hashed_password)



