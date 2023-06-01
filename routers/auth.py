from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session

from .. import db, schemas

router = APIRouter(tags=['Authentication'])

# @router.post("/login")
# def login(admin_credentials: schemas.AdminLogin, db: Session = Depends(db.get_db))
