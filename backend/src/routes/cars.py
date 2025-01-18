from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.models.car import Car, CarCreate
from src.utils.database import get_db
from typing import List

router = APIRouter()

@router.get("/cars/", response_model=List[Car])
def read_cars(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    cars = db.query(Car).offset(skip).limit(limit).all()
    return cars

@router.get("/cars/{car_id}", response_model=Car)
def read_car(car_id: int, db: Session = Depends(get_db)):
    car = db.query(Car).filter(Car.id == car_id).first()
    if not car:
        raise HTTPException(status_code=404, detail="Car not found")
    return car

@router.post("/cars/", response_model=Car)
def create_car(car: CarCreate, db: Session = Depends(get_db)):
    db_car = Car(**car.dict())  # Create a new instance of your SQLAlchemy model
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car

@router.put("/cars/{car_id}", response_model=Car)
def update_car(car_id: int, car: CarCreate, db: Session = Depends(get_db)):
    db_car = db.query(Car).filter(Car.id == car_id).first()
    if not db_car:
        raise HTTPException(status_code=404, detail="Car not found")
    for key, value in car.dict().items():
        setattr(db_car, key, value)  # Update each field
    db.commit()
    db.refresh(db_car)
    return db_car

@router.delete("/cars/{car_id}")
def delete_car(car_id: int, db: Session = Depends(get_db)):
    db_car = db.query(Car).filter(Car.id == car_id).first()
    if not db_car:
        raise HTTPException(status_code=404, detail="Car not found")
    db.delete(db_car)
    db.commit()
    return {"message": "Car deleted successfully"}
