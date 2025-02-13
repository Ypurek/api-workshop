def test_me(session):
    response = session.get('http://shopen.qamania.org/api/v1/users/me')
    assert response.status_code == 200
    assert response.json()['id'] > 0


def test_get_pens(session):
    response = session.get('http://shopen.qamania.org/api/v1/pens')
    assert response.status_code == 200
    assert len(response.json()['pens']) > 3


def test_buy(buy):
    session, penId = buy
    session.post('http://shopen.qamania.org/api/v1/transactions/request', json={
  "order": [
    {
      "id": penId,
      "count": 10
    }
  ]
})