from typing import Union 
from fastapi import FastAPI
from models.item_model import Item

# creacion de una aplicacion

app= FastAPI()

@app.get("/")
def read_root():
    return {"si yo digo que si": "mundo"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get('/calculador')
def calcular(operador_1: float, operador_2: float ):
    return {'suma': operador_1 + operador_2}

@app.put('/items/({item_id}')
def update_item(item_id: int, item: Item):
    return {'item_name': item.name, 'item_id': item_id, 'item_price':item.price}