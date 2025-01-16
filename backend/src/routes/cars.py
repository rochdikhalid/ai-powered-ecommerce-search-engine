from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.utils.database import session
from src.models.car import Car


router = APIRouter()

@router.get("/cars/")
def read_cars(skip: int = 0, limit: int = 100, db: Session = Depends()):
    return db.query(Car).offset(skip).limit(limit).all()

@router.get("/cars/{car_id}")
def read_car(car_id: int, db: Session = Depends()):
    return db.query(Car).filter(Car.id == car_id).first()

@router.post("/cars/")
def create_car(car: Car, db: Session = Depends()):
    db.add(car)
    db.commit()
    db.refresh(car)
    return car

@router.put("/cars/{car_id}")
def update_car(car_id: int, car: Car, db: Session = Depends()):
    db_car = db.query(Car).filter(Car.id == car_id).first()
    if db_car:
        db_car.make = car.make
        db_car.model = car.model
        db_car.year = car.year
        db_car.price = car.price
        db_car.transmission = car.transmission
        db_car.fuel_type = car.fuel_type
        db.commit()
        db.refresh(db_car)
        return db_car
    else:
        return {"error": "Car not found"}

@router.delete("/cars/{car_id}")
def delete_car(car_id: int, db: Session = Depends()):
    db_car = db.query(Car).filter(Car.id == car_id).first()
    if db_car:
        db.delete(db_car)
        db.commit()
        return {"message": "Car deleted successfully"}
    else:
        return {"error": "Car not found"}