from fastapi import FastAPI
from fastapi.response import HTMLResponse

app = FastAPI()

app.title = "My Awesome API"
app.version = "1.0.0"

@app.get("/",tags=['home'])
def message():
    return HTMLResponse(content = "<h1>Hola Mundo!!!!</h1>")