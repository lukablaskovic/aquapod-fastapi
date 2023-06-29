from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import aquapod, user, auth

from .db import engine, get_db
from . import schemas
from . import models
from sqlalchemy.orm import Session

import csv

models.Base.metadata.create_all(bind=engine)

origins = [
    "http://localhost:5173",
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"msg": "FASTAPI REST API - Running ✅"}


@app.on_event("startup")
async def add_units_instances():
    db: Session = Session(bind=engine)

    if db.query(models.Unit).first() is None:
        with open("units.csv", "r") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                unit = schemas.UnitCreate(
                    name=row[0], symbol=row[1], description=row[2]
                )
                new_unit = models.Unit(**unit.dict())
                db.add(new_unit)
        db.commit()
        print("Units added to database")


app.include_router(aquapod.router)
app.include_router(user.router)
app.include_router(auth.router)
# Run with: uvicorn app.main:app --reload
