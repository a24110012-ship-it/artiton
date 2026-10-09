from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_crear_artesania_retorna_201():
    payload = {"nombre": "Alebrije de madera", "precio": 500.00}
    response = client.post("/artesanias/", json=payload)

    assert response.status_code == 201
    assert response.json()["nombre"] == "Alebrije de madera"