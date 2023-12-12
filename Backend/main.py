from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from config.database import engine, Base

app = FastAPI()

app.title = "Recomendador de Contraseñas"
app.version = "1.0.0"

Base.metadata.create_all(bind=engine)

@app.get("/",tags=['home'])
def message():
    return HTMLResponse(content = "<h1>Hola Mundo!!!!</h1>")