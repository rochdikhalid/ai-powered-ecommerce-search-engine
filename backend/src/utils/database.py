from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models.car import Base


DATABASE_URL = "postgresql://user:password@db:5432/postgres"

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()