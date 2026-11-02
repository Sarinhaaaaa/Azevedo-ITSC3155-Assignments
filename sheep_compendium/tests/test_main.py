from fastapi.testclient import TestClient
from main import app
client = TestClient(app)

def test_read_sheep ():
    response = client.get("/sheep/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "Spice",
        "breed": "Gotland",
        "sex": "ewe"
}

def test_add_sheep():
    new_sheep = {
        "id": 7,
        "name": "Babe",
        "breed": "Suffolk",
        "sex": "ram"
    }
    response = client.post("/sheep/", json=new_sheep)
    assert response.status_code == 201
    assert response.json() == new_sheep


def test_delete_sheep():
    response = client.delete("/sheep/1")
    assert response.status_code == 204
    check_response = client.get("/sheep/1")
    assert check_response.status_code == 404


def test_update_sheep():
    updated_sheep = {
        "id": 5,
        "name": "Sweetie",
        "breed": "Gotland",
        "sex": "ewe"
    }
    response = client.put("/sheep/5", json=updated_sheep)
    assert response.status_code == 200
    assert response.json() == updated_sheep
    bad_response = client.put("/sheep/999", json=updated_sheep)
    assert bad_response.status_code == 404


def test_read_all_sheep():
    response = client.get("/sheep/")
    assert response.status_code == 200
    sheep_list = response.json()
    assert isinstance(sheep_list, list)
    assert len(sheep_list) > 0