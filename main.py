# main.py
from fastapi import FastAPI
from schemas import Artesania

app = FastAPI()

@app.post("/artesanias/", status_code=201)
def crear_artesania(artesania: Artesania):
    return {"nombre": artesania.nombre, "precio": artesania.precio}