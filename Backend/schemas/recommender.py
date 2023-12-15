
# The `Recommender` class is a Pydantic model that represents a recommender with an optional ID and a
# required password field with a minimum length of 8 characters and a maximum length of 20 characters.
from pydantic import BaseModel, Field
from typing import Optional

class Recommender(BaseModel):
    id: Optional[int] = None
    password:str= Field(min_length=8, max_length=20)