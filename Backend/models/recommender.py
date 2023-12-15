# The code is importing the `Base` class from the `config.database` module and the `Column`,
# `Integer`, and `String` classes from the `sqlalchemy` module.
from config.database import Base 
from sqlalchemy import Column, Integer, String

# The class "Recommender" is a subclass of "Base" and represents a table named "recommender" with
# columns "id" and "password".
class Recommender(Base):
    __tablename__ = "recommender"

    id = Column(Integer, primary_key=True, index=True)
    password = Column(String, nullable=False)