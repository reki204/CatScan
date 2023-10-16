import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200

def test_result_route(client):
    response = client.get('/result')
    assert response.status_code == 200

def test_profile_route(client):
    response = client.get('/profile')
    assert response.status_code == 200

def test_book_route(client):
    response = client.get('/book')
    assert response.status_code == 200
