from fastapi import APIRouter, Depends, Path, Query
from fastapi.responses import JSONResponse
from typing import List
from config.database import Session
from models.recommender import Recommender
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
import time
from schemas.recommender import Recommender

Recommender_router = APIRouter()

@Recommender_router.get("/recommender", tags=['Recommender'], response_model=List[Recommender], status_code=200, dependencies=[Depends(JWTBearer())])
def get_recommender():
    db = Session()
    result = db.query(Recommender).all()
    db.close()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))