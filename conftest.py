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
def buy(session) -> tuple[requests.Session, int]:
    response = requests.post('http://shopen.qamania.org/api/v1/users/login', json={
        "username": "admin",
        "password": "admin"
    })
    admin_token = response.json()['token']
    response = session.get('http://shopen.qamania.org/api/v1/users/me')
    userId = response.json()['id']
    requests.patch(f'http://shopen.qamania.org/api/v1/users/user/{userId}/credit?credit=1000',
                   headers={'Authorization': admin_token})
    response = requests.post(f'http://shopen.qamania.org/api/v1/pens/add', json={
        "brand": "parker",
        "price": 10,
        "stock": 100,
        "color": "red",
        "length": 15
    },
                   headers={'Authorization': admin_token})

    return session, response.json()['id']
