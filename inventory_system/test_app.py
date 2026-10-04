import pytest
import sys
import os

# Add the parent directory to path so we can find app
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from inventory_system.app import app 

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        from inventory_system.app import items
        items.clear()
        yield client

def test_get_empty_inventory(client):
    response = client.get('/inventory')
    assert response.status_code == 200
    assert response.json == []

def test_add_item(client):
    response = client.post('/inventory', 
                          json={'name': 'Apple', 'price': 1.99, 'stock': 10})
    assert response.status_code == 201
    assert response.json['name'] == 'Apple'
    assert response.json['id'] == 1

def test_get_one_item(client):
    client.post('/inventory', json={'name': 'Banana', 'price': 0.99, 'stock': 5})
    response = client.get('/inventory/1')
    assert response.status_code == 200
    assert response.json['name'] == 'Banana'

def test_update_item(client):
    client.post('/inventory', json={'name': 'Orange', 'price': 2.99, 'stock': 3})
    response = client.patch('/inventory/1', json={'price': 3.99})
    assert response.status_code == 200
    assert response.json['price'] == 3.99

def test_delete_item(client):
    client.post('/inventory', json={'name': 'Grape', 'price': 4.99, 'stock': 2})
    client.delete('/inventory/1')
    response = client.get('/inventory')
    assert response.json == []