from fastapi import FastAPI, HTTPException
from schemas import Artesania

app = FastAPI()

@app.post("/artesanias/", status_code=201)
def crear_artesania(artesania: Artesania):
    if artesania.precio < 0:
        raise HTTPException(status_code=400, detail="El precio no puede ser negativo")
    return {"nombre": artesania.nombre, "precio": artesania.precio}