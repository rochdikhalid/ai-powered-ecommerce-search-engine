from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Car(Base):
    __tablename__ = "cars"
    id = Column(Integer, primary_key=True)
    make = Column(String)
    model = Column(String)
    year = Column(Integer)
    price = Column(Float)
    transmission = Column(String)
    fuel_type = Column(String)

    def __repr__(self):
        return f"Car(id={self.id}, make={self.make}, model={self.model}, year={self.year}, price={self.price}, transmission={self.transmission}, fuel_type={self.fuel_type})"