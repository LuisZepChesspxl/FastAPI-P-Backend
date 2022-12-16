from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import json

from models.item_model import cliente

app = FastAPI()

app.mount("/static", StaticFiles(directory="./public/static"), name="static")

templates = Jinja2Templates(directory="./public/templates")

@app.get('/index/', response_class=HTMLResponse)
def index(request: Request):
    context = {'request': request}
    return templates.TemplateResponse("index.html", context)

@app.post("/cliente")
def regclient(cliente: cliente):
    return {cliente.nombre, cliente.no_telefono, cliente.ciudad,cliente.estado,cliente.tipo,cliente.ctarj}