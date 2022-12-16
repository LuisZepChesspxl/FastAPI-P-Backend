from pydantic import BaseModel
from typing import Union 

#class Item(BaseModel):
 #   name: str
#  price: float
#    is_offer: Union[bool, None]= None

class cliente(BaseModel):
    nombre: str
    no_telefono: int
    ciudad: str
    estado: str
    tipo: str
    ctarj: int