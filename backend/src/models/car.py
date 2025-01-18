from pydantic import BaseModel
from typing import Optional

class CarBase(BaseModel):
    make: str
    model: str
    year: int
    price: float
    transmission: str
    fuel_type: str

class CarCreate(CarBase):
    pass

class Car(CarBase):
    id: int

    class Config:
        from_attributes = True