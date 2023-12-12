from config.database import Base 
from sqlalchemy import Column, Integer, String, Float

class Recommender(Base):
    __tablename__ = "recommender"

    id = Column(Integer, primary_key=True, index=True)
    password = Column(String, nullable=False)