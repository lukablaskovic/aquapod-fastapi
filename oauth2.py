from jose import JWTError, jwt
from datetime import datetime, timedelta
import os
# SECRET_KEY
# Algorithm
# Exp time

SECRET_KEY = os.getenv("JWT_SECRET")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 3600


def create_access_token(data: dict):
    to_encode = data.copy()
    expire_time = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire_time})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
