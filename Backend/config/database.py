# The code is importing necessary modules from the SQLAlchemy library.
import os 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from sqlalchemy.ext.declarative import declarative_base 


sqlite_file_name = "../database.sqlite" # Database file name
base_dir = os.path.dirname(os.path.realpath(__file__)) # Application Base Directory

database_url = f"sqlite:///{os.path.join(base_dir, sqlite_file_name)}" # Database URL

engine = create_engine(database_url, echo=True) # Creating the database engine

Session = sessionmaker(bind=engine) # Creating the database session

Base = declarative_base() # creation of the database