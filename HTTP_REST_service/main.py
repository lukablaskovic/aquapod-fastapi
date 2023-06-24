from fastapi import FastAPI

import os
import models
from db import engine, get_db
from routers import aquapod, user, auth


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
async def root():
    return {"msg": "Hello World!"}


app.include_router(aquapod.router)
app.include_router(user.router)
app.include_router(auth.router)
# Run with: uvicorn main:app --reload
