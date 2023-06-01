from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

import db
import schemas
import models
import utils
import oauth2

router = APIRouter(prefix="/auth", tags=['Authentication'])


@router.post("/")
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(db.get_db)):
    # returns username, password
    user = db.query(models.User).filter(
        models.User.email == user_credentials.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials")
    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials")
    access_token = oauth2.create_access_token(
        data={"user_id": user.id, "user_email": user.email})
    return {"access_token": access_token, "token_type": "Bearer"}

# 7:13:39
