from settings import BASE_URL


def test_me(session):
    response = session.get(f'{BASE_URL}/users/me')
    assert response.status_code == 200
    assert response.json()['id'] > 0


def test_get_pens(session):
    response = session.get(f'{BASE_URL}/pens')
    assert response.status_code == 200
    assert len(response.json()['pens']) > 3


def test_buy(buy):
    session, penId = buy
    session.post(f'{BASE_URL}/transactions/request', json={
        "order": [
            {
                "id": penId,
                "count": 10
            }
        ]
    })
