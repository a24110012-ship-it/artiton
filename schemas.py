# schemas.py
from pydantic import BaseModel

class Artesania(BaseModel):
    nombre: str
    precio: float