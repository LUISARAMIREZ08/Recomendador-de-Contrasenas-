#The User class defines a user model with email and password attributes.
from pydantic import BaseModel

class User(BaseModel):
    email: str
    password: str 