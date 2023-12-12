from pydantic import BaseModel, Field
from typing import Optional

class Recommender(BaseModel):
    id: Optional[int] = None
    password: Field(str, min_length=8, max_length=20)