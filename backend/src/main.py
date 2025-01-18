from fastapi import FastAPI
from src.routes.cars import router as cars_router

app = FastAPI()

# Include the car routes
app.include_router(cars_router, prefix="/api", tags=["cars"])
