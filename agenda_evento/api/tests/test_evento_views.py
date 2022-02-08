from django.test import Client


def test_deve_criar_evento(client: Client):
    data_requests = {
        "titulo": "Call de Alinhamento",
        "data": "09/12/2021",
        "horario_inicio": "16:40",
        "horario_fim": "17:08",
        "convidados": ["janiojs@icloud.com"],
        "local": "https://meet.google.com/rbr-hhfr-mnt",
        "descricao": "Call para alinhar próximos módulos do curso"
    }

    response = client.post(path='/api/v1/eventos', data=data_requests)

    assert response.status_code == 201

    response_mensagem = response.data['mensagem']
    assert response_mensagem == 'Dados recebidos com sucesso'

    dados = response.data['dados']
    assert dados['titulo'] == 'Call de Alinhamento'
    assert dados['data'] == '09/12/2021'
    assert dados['horario_inicio'] == '16:40'
    assert dados['horario_fim'] == '17:08'
    assert dados['convidados'] == 'janiojs@icloud.com'
    assert dados['local'] == 'https://meet.google.com/rbr-hhfr-mnt'
    assert dados['descricao'] == 'Call para alinhar próximos módulos do curso'


def test_deve_listar_evento(client: Client):
    response = client.get('/api/v1/eventos')

    assert response.status_code == 200

    dados = response.data[0]
    assert dados['titulo'] == 'Call de Alinhamento'
    assert dados['data'] == '09/12/2021'
    assert dados['horario_inicio'] == '16:40'
    assert dados['horario_fim'] == '17:00'
    assert dados['convidados'] == ['janiojs@icloud.com']
    assert dados['local'] == 'https://meet.google.com/rbr-hhfr-mnt'
    assert dados['descricao'] == 'Call para alinhar próximos módulos do curso'
