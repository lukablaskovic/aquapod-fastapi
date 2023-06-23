from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body

# For automatic datatype validation
from typing import Optional, List

import psycopg2 as psy
from psycopg2.extras import RealDictCursor

from sqlalchemy.orm import Session
import models
import schemas
import utils
from db import engine, get_db
from routers import aquapod, user, auth

models.Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.get("/")
def root():
    return {"msg": "Hello World!"}


app.include_router(aquapod.router)
app.include_router(user.router)
app.include_router(auth.router)
# Run with: uvicorn main:app --reload
