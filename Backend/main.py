# Description: Application main file

# The following lines of code import several modules and classes from different files and packages.
from fastapi import FastAPI 
from fastapi.responses import HTMLResponse 
from config.database import engine, Base
from routers.auth import auth_router
from routers.recommender import Recommender_router
from middlewares.error_handler import ErrorHandler

# An instance of the `FastAPI` class is created, which is a class provided by the FastAPI framework.
app = FastAPI()

# The lines `app.title = "Recomendador de Contraseñas"` and `app.version = "1.0.0"` are setting the
# title and version of the FastAPI application.
app.title = "Recomendador de Contraseñas"
app.version = "1.0.0"

# The lines `app.add_middleware(ErrorHandler)`, `app.include_router(auth_router)`, and
# `app.include_router(Recommender_router)` are adding middleware and routers to the FastAPI
# application.
app.add_middleware(ErrorHandler)
app.include_router(auth_router)
app.include_router(Recommender_router)

# `Base.metadata.create_all(bind=engine)` is a line of code that creates all the tables defined in the
# database schema.
Base.metadata.create_all(bind=engine)

# The function `message` returns an HTML response with the message "Hola Crea tu contraseña!!!!".
@app.get("/",tags=['home'])
def message():
    return HTMLResponse(content = "<h1>Hola Crea tu contraseña!!!!</h1>")

