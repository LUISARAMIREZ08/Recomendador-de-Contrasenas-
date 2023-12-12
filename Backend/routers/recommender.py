from fastapi import APIRouter, Depends, Path, Query
from fastapi.responses import JSONResponse
from typing import List
from config.database import Session
from models.recommender import Recommender as ModelRecommender
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
import time
from schemas.recommender import Recommender
import secrets
import string
import random


Recommender_router = APIRouter()

@Recommender_router.get("/recommender", tags=['Recommender'], response_model=List[Recommender], status_code=200, dependencies=[Depends(JWTBearer())])
def get_recommender():
    db = Session()
    result = db.query(ModelRecommender).all()
    db.close()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@Recommender_router.get("/recommender/{id}", tags=['Recommender'], response_model=Recommender, status_code=200, dependencies=[Depends(JWTBearer())])
def get_recommender_by_id(id: int = Path(..., gt=0)):
    db = Session()
    result = db.query(ModelRecommender).filter(ModelRecommender.id == id).first()
    db.close()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@Recommender_router.post("/recommender/create", tags=['Recommender'], response_model=Recommender, status_code=201, dependencies=[Depends(JWTBearer())])
def create_recommender(recommender: Recommender):
    db = Session()
    new_password = ModelRecommender(**recommender.model_dump())
    db.add(new_password)
    db.commit()
    return JSONResponse(content={"message":"Movie created successfully"}, status_code=201)

@Recommender_router.put("/recommender/update/{id}", tags=['Recommender'])
def update_recommender(id: int, recommender: Recommender):
    db = Session()
    result = db.query(ModelRecommender).filter(ModelRecommender.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={"message":"Password not found"})
    result.password = recommender.password
    db.commit()
    return JSONResponse(status_code=200, content={"message":"Password updated successfully"})

@Recommender_router.delete("/recommender/delete/{id}", tags=['Recommender'], status_code=200, dependencies=[Depends(JWTBearer())])
def delete_recommender(id: int):
    db = Session()
    result = db.query(ModelRecommender).filter(ModelRecommender.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={"message":"Password not found"})
    db.delete(result)
    db.commit()
    return JSONResponse(status_code=200, content={"message":"Password deleted successfully"})

@Recommender_router.post("/recommender/generate_password", tags=['Recommender'], response_model=str, status_code=200, dependencies=[Depends(JWTBearer())])
def generate_password(minusculas: int = Query(..., ge=0), mayusculas: int = Query(..., ge=0),
                       numeros: int = Query(..., ge=0), caracteres_especiales: int = Query(..., ge=0)):
    db = Session()
    contraseña = []

    for i in range(minusculas):
        contraseña.append(secrets.choice(string.ascii_lowercase))

    for i in range(mayusculas):
        contraseña.append(secrets.choice(string.ascii_uppercase))

    for i in range(numeros):
        contraseña.append(secrets.choice(string.digits))

    for i in range(caracteres_especiales):
        contraseña.append(secrets.choice(string.punctuation))

    random.shuffle(contraseña)
    contraseña_final = "".join(contraseña)

    new_recommender = ModelRecommender(password=contraseña_final)

    db.add(new_recommender)
    db.commit()

    return JSONResponse(status_code=200, content={"password": contraseña_final})
