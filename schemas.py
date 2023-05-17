from pydantic import BaseModel

# Schema/Pydantic model defines the structure of a request & response


class AquaPodBase(BaseModel):
    name: str


class AquaPodCreate(AquaPodBase):
    pass


class AquaPod(AquaPodBase):
    id: int

    class Config:
        orm_mode = True
