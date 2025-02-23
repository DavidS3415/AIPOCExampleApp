import json
import pytest

def test_get_users_empty(client):
    # Initially, the user list should be empty
    response = client.get('/users')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data == []  

def test_create_user(client):
    new_user = {"name": "Test User", "email": "test@example.com"}
    
    # Create a new user via POST request
    response = client.post(
        '/users',
        data=json.dumps(new_user),
        content_type='application/json'
    )
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['name'] == new_user['name']
    assert data['email'] == new_user['email']
    
    # Verify the user is now in the list
    response = client.get('/users')
    data = json.loads(response.data)
    assert any(user['email'] == new_user['email'] for user in data)

def test_get_user_by_id(client):
    new_user = {"name": "Test User", "email": "test@example.com"}
    
    # Create a user first
    response = client.post(
        '/users',
        data=json.dumps(new_user),
        content_type='application/json'
    )
    data = json.loads(response.data)
    user_id = data.get('id')  
    
    # Retrieve the user by id
    response = client.get(f'/users/{user_id}')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['name'] == new_user['name']
    assert data['email'] == new_user['email']