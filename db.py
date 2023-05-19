from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DB = {
    "provider": "postgres",
    "user": os.getenv("UVICORN_USER"),
    "password": os.getenv("UVICORN_PASSWORD"),
    "host": os.getenv("UVICORN_HOST"),
    "database": os.getenv("UVICORN_DATABASE")
}
print(DB)

SQLALCHEMY_DATABASE_URL = f"postgresql://{DB['user']}:{DB['password']}@{DB['host']}/{DB['database']}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
