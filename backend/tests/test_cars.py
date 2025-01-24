import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.routes.cars import router
from src.models.car_sqlalchemy import Base, CarSQLAlchemy
from src.main import app

# Test database setup
DATABASE_URL = "sqlite:///./test.db" 
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency override for tests
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.include_router(router)
app.dependency_overrides[override_get_db] = override_get_db

client = TestClient(app)

@pytest.fixture(scope="function", autouse=True)
def setup_test_database():
    Base.metadata.create_all(bind=engine)
    
    db = TestingSessionLocal()
    test_cars = [
        CarSQLAlchemy(make="Toyota", model="Corolla", year=2020, price=20000, transmission="Automatic", fuel_type="Gasoline"),
        CarSQLAlchemy(make="Ford", model="Focus", year=2019, price=15000, transmission="Manual", fuel_type="Diesel"),
    ]
    db.add_all(test_cars)
    db.commit()
    db.close()
    
    yield
    
    Base.metadata.drop_all(bind=engine)

def test_search_cars():
    response = client.get("/search/?query=Toyota")
    assert response.status_code == 200
    results = response.json()
    assert len(results) > 0
    assert results[0]["make"] == "Toyota"

def test_search_no_matching_cars():
    response = client.get("/search/?query=NonExistentCar")
    assert response.status_code == 200
    results = response.json()
    assert len(results) == 0  

def test_search_multiple_matching_cars():
    response = client.get("/search/?query=Car")
    assert response.status_code == 200
    results = response.json()
    assert len(results) > 1 
    assert results[0]["make"] in ["Toyota", "Ford"] 
    assert results[1]["make"] in ["Toyota", "Ford"]

