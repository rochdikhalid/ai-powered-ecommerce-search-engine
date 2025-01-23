from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from src.utils.database import get_db
from src.models.car_sqlalchemy import CarSQLAlchemy
from src.nlp_model import NLPModel
import numpy as np

router = APIRouter()

nlp_model = NLPModel()

@router.get("/search/")
def search_cars(query: str, db: Session = Depends(get_db)):
    # Get the query embedding
    query_embedding = nlp_model.get_embeddings(query)

    # Fetch all cars and calculate similarity score
    cars = db.query(CarSQLAlchemy).all()
    results = []
    for car in cars:
        car_embedding = nlp_model.get_embeddings(car.make + " " + car.model)
        similarity = np.dot(query_embedding, car_embedding) / (np.linalg.norm(query_embedding) * np.linalg.norm(car_embedding))
        results.append((car, similarity))

    # Sort results by similarity score and return top 10
    results.sort(key=lambda x: x[1], reverse=True)
    return [car for car, _ in results[:10]]
