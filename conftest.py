import pytest
import requests
import uuid

BASE_URL = 'http://shopen.qamania.org/api/v1'


@pytest.fixture(scope='session')
def session():
    s = requests.Session()
    response = s.post(f'{BASE_URL}/users/register', json={
        "username": str(uuid.uuid4()),
        "password": "testing"
    })
    s.headers.update({
        'Authorization': response.json()['token']
    })
    return s


@pytest.fixture
def admin():
    s = requests.Session()
    response = s.post(f'{BASE_URL}/users/login', json={
        "username": "admin",
        "password": "admin"
    })
    s.headers.update({
        'Authorization': response.json()['token']
    })
    return s

@pytest.fixture
def buy(session, admin) -> tuple[requests.Session, int]:
    response = session.get('http://shopen.qamania.org/api/v1/users/me')
    userId = response.json()['id']
    admin.patch(f'http://shopen.qamania.org/api/v1/users/user/{userId}/credit?credit=1000')
    response = admin.post(f'http://shopen.qamania.org/api/v1/pens/add', json={
        "brand": "parker",
        "price": 10,
        "stock": 100,
        "color": "red",
        "length": 15
    })

    return session, response.json()['id']
