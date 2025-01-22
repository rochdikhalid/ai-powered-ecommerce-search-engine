from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class CarSQLAlchemy(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True, index=True)
    make = Column(String, index=True)
    model = Column(String)
    year = Column(Integer)
    price = Column(Float)
    transmission = Column(String)
    fuel_type = Column(String)