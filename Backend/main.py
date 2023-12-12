from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from config.database import engine, Base
from routers.recommender import Recommender_router
from middlewares.error_handler import ErrorHandler

app = FastAPI()

app.title = "Recomendador de Contraseñas"
app.version = "1.0.0"

app.add_middleware(ErrorHandler)
app.include_router(Recommender_router)

Base.metadata.create_all(bind=engine)

@app.get("/",tags=['home'])
def message():
    return HTMLResponse(content = "<h1>Hola Mundo!!!!</h1>")