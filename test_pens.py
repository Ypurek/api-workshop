import pytest
from settings import BASE_URL


@pytest.mark.parametrize('length', [1, 5, 50, 100, 1000])
def test_create_pens_positive(admin, length):
    response = admin.post(f'{BASE_URL}/pens/add', json={
        "brand": "parker",
        "price": 10,
        "stock": 100,
        "color": "red",
        "length": length
    })
    assert response.status_code == 201


@pytest.mark.parametrize('length', [0, -1, -5, 'a', True, None])
def test_create_pens_negative(admin, length):
    response = admin.post(f'{BASE_URL}/pens/add', json={
        "brand": "parker",
        "price": 10,
        "stock": 100,
        "color": "red",
        "length": length
    })
    assert response.status_code == 400
