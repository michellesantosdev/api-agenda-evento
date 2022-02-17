import pytest

from django.test import Client


pytestmark = [pytest.mark.django_db]


def test_deve_remover_evento(client: Client):
    # GIVEN
    request = {
        'titulo': 'Call de Alinhamento',
        'data': '2021-12-09',
        'horario_inicio': '13:30',
        'horario_fim': '17:00',
        'convidados': ['minha.mãe@gmail.com'],
        'local': 'https://meet.google.com/rbr-hhfr-mnt',
        'descricao': 'Call para alinhar próximos módulos do curso'
    }
    response_post = client.post('/api/v1/eventos', data=request, content_type='application/json')
    id_evento_criado = response_post.data['evento_id']

    # WHEN
    response_delete = client.delete(f'/api/v1/eventos/{id_evento_criado}')

    # THEN
    assert response_delete.status_code == 201
    assert response_delete.data['id'] == str(id_evento_criado)
    assert response_delete.data['message'] == 'Evento removido com sucesso.'

    response_get = client.get(f'/api/v1/eventos/{id_evento_criado}')
    assert response_get.status_code == 404
    assert response_get.data == {'detail': 'Not found.'}


def test_deve_atualizar_um_campo_do_evento(client: Client):
    # GIVEN
    body = {
        'titulo': 'Call de Alinhamento',
        'data': '2021-12-09',
        'horario_inicio': '13:30',
        'horario_fim': '17:00',
        'convidados': ['minha.mãe@gmail.com'],
        'local': 'https://meet.google.com/rbr-hhfr-mnt',
        'descricao': 'Call para alinhar próximos módulos do curso'
    }
    response_post = client.post('/api/v1/eventos', data=body, content_type='application/json')
    id_evento_criado = response_post.data['evento_id']

    # WHEN
    body_put = {
        'titulo': 'Call de Alinhamento - Editado'
    }
    response = client.put(f'/api/v1/eventos/{id_evento_criado}', data=body_put, content_type='application/json')

    # THEN
    assert response.status_code == 200
    data = response.data
    assert data['titulo'] == 'Call de Alinhamento - Editado'
    assert data['data'] == '2021-12-09'
    assert data['horario_inicio'] == '13:30:00'
    assert data['horario_fim'] == '17:00:00'
    assert data['convidados'] == ['minha.mãe@gmail.com']
    assert data['local'] == 'https://meet.google.com/rbr-hhfr-mnt'
    assert data['descricao'] == 'Call para alinhar próximos módulos do curso'


def test_deve_listar_evento_por_id(client: Client):
    # GIVEN
    request = {
        'titulo': 'Call de Alinhamento',
        'data': '2021-12-09',
        'horario_inicio': '13:30',
        'horario_fim': '17:00',
        'convidados': ['minha.mãe@gmail.com'],
        'local': 'https://meet.google.com/rbr-hhfr-mnt',
        'descricao': 'Call para alinhar próximos módulos do curso'
    }
    response_post = client.post('/api/v1/eventos', data=request, content_type='application/json')
    id_evento_criado = response_post.data['evento_id']

    # WHEN
    response = client.get(f'/api/v1/eventos/{id_evento_criado}')

    # THEN
    assert response.status_code == 200
    data = response.data
    assert data['titulo'] == 'Call de Alinhamento'
    assert data['data'] == '2021-12-09'
    assert data['horario_inicio'] == '13:30:00'
    assert data['horario_fim'] == '17:00:00'
    assert data['convidados'] == ['minha.mãe@gmail.com']
    assert data['local'] == 'https://meet.google.com/rbr-hhfr-mnt'
    assert data['descricao'] == 'Call para alinhar próximos módulos do curso'


def test_nao_deve_listar_evento_nao_encontrado(client: Client):
    # GIVEN
    # WHEN
    response = client.get(f'/api/v1/eventos/100')

    # THEN
    assert response.status_code == 404
    assert response.data == {'detail': 'Not found.'}


def test_deve_listar_evento(client: Client):
    data_requests = {
        "titulo": "Call de Alinhamento",
        "data": "2021-12-09",
        "horario_inicio": "16:40",
        "horario_fim": "17:08",
        "convidados": ["janiojs@icloud.com"],
        "local": "https://meet.google.com/rbr-hhfr-mnt",
        "descricao": "Call para alinhar próximos módulos do curso"
    }
    client.post(path='/api/v1/eventos', data=data_requests)

    response = client.get('/api/v1/eventos')

    assert response.status_code == 200

    dados = response.data[0]
    assert dados['titulo'] == 'Call de Alinhamento'
    assert dados['data'] == '2021-12-09'
    assert dados['horario_inicio'] == '16:40:00'
    assert dados['horario_fim'] == '17:08:00'
    assert dados['convidados'] == ['janiojs@icloud.com']
    assert dados['local'] == 'https://meet.google.com/rbr-hhfr-mnt'
    assert dados['descricao'] == 'Call para alinhar próximos módulos do curso'


def test_deve_criar_evento(client: Client):
    data_requests = {
        "titulo": "Call de Alinhamento",
        "data": "2021-12-09",
        "horario_inicio": "16:40",
        "horario_fim": "17:08",
        "convidados": ["janiojs@icloud.com"],
        "local": "https://meet.google.com/rbr-hhfr-mnt",
        "descricao": "Call para alinhar próximos módulos do curso"
    }

    response = client.post(path='/api/v1/eventos', data=data_requests)

    assert response.status_code == 201

    response_mensagem = response.data['message']
    assert response_mensagem == 'Evento Call de Alinhamento criado com sucesso.'
