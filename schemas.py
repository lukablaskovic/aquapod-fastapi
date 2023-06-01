from pydantic import BaseModel, EmailStr
from typing import Optional, List

# Schema/Pydantic model defines the structure of a request & response


class AquaPodBase(BaseModel):
    name: str


class AquaPodCreate(AquaPodBase):
    pass


class AquaPod(AquaPodBase):
    id: int

    class Config:
        orm_mode = True


class PumpCreate(BaseModel):
    aquapod_id: int
    speed: int = 0
    working_time: float = 0.0
    alarm_status: Optional[str] = None


class Pump(PumpCreate):
    id: int
    speed_unit_id: int

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True
