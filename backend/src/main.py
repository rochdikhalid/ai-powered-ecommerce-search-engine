from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes.cars import router as cars_router

app = FastAPI()

# Include the car routes
app.include_router(cars_router, prefix="/api", tags=["cars"])

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],
)
