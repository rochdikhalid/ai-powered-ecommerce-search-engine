import pandas as pd
from sqlalchemy import create_engine
from src.models.car_sqlalchemy import CarSQLAlchemy, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


# Load the dataset
df = pd.read_csv("/app/data/car_details_v4.csv")

# Database connection
DATABASE_URL = "postgresql://user:password@db:5432/mydatabase"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()

# Create the table if not already created
Base.metadata.create_all(bind=engine)

# Insert data into the database
for index, row in df.iterrows():
    car = CarSQLAlchemy(
        make=row['Make'],
        model=row['Model'],
        year=row['Year'],
        price=row['Price'],
        transmission=row['Transmission'],
        fuel_type=row['Fuel Type']
    )
    session.add(car)
session.commit()
