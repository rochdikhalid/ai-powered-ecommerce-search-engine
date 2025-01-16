from fastapi import FastAPI 
from src.routes.cars import router
from src.utils.database import engine


app = FastAPI()

app.include_router(router)

@app.lifespan("shutdown")
def shutdown_event():
    engine.dispose()