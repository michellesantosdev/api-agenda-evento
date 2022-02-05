from django.test import Client


def test_home_status_code(client: Client):
    response = client.get('/teste')
    assert response.status_code == 200


def test_home_content(client: Client):
    response = client.get('/teste')
    assert response.content == b'Oi, cliente'
