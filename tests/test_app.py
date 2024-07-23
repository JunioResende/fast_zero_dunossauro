from http import HTTPStatus as HTTPSStatus

from fastapi.testclient import TestClient

from fast_zero.app import app

client = TestClient(app)


def test_read_root_deve_retornar_e_ola_mundo():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == HTTPSStatus.OK
    assert response.json() == {'message': 'Ola mundo'}
