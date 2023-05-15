from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body

# For automatic datatype validation
from pydantic import BaseModel
from typing import Optional

import psycopg2 as psy
from psycopg2.extras import RealDictCursor

from sqlalchemy.orm import Session
from . import models
from .db import engine, get_db

models.Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.get("/")
def root():
    return {"msg": "Hello World!"}


@app.get("/sqlaclhemy")
def test(db: Session = Depends(get_db)):
    aquapods = []
    try:
        aquapods = db.query(models.AquaPod).all()
    except Exception as e:
        print(e)
    return {"data": aquapods}

# Run with uvicorn app.main:app --reload
