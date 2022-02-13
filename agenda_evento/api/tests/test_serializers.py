import datetime
import pytest

from ..serializers import EventSerializer


pytestmark = [pytest.mark.django_db]


def test_deve_deserializar_evento():
    dados_do_evento = {  # json/dict
        'titulo': 'Call para Alinhar 2',
        'data': datetime.datetime.now().date(),
        'horario_inicio': datetime.datetime.now().time(),
        'horario_fim': datetime.datetime.now().time(),
        'convidados': ['israel.silva@gmail.com', 'janio.silva@gmail.com'],
        'local': 'Google Meet',
        'descricao': 'Call de alinhamento dos novos módulos do curso'
    }

    evento_serializado = EventSerializer(data=dados_do_evento)  # evento_ser... objeto
    evento_serializado.is_valid()
    evento_objeto = evento_serializado.save()

    assert evento_objeto.titulo == 'Call para Alinhar 2'
    assert evento_objeto.data is not None
    assert evento_objeto.horario_inicio is not None
    assert evento_objeto.horario_fim is not None
    assert evento_objeto.convidados == ['israel.silva@gmail.com', 'janio.silva@gmail.com']
    assert evento_objeto.local == 'Google Meet'
    assert evento_objeto.descricao == 'Call de alinhamento dos novos módulos do curso'


def test_deve_serializer_evento(evento):
    evento_serializado = EventSerializer(evento)  # evento é um objeto

    assert len(evento_serializado.data) == 8  # evento_serializado é um json/dict
    assert evento_serializado.data['titulo'] == 'Call para Alinhar'
    assert evento_serializado.data['data'] is not None
    assert evento_serializado.data['horario_inicio'] == '13:00:00'
    assert evento_serializado.data['horario_fim'] == '13:30:00'
    assert evento_serializado.data['convidados'] == ['israel.silva@gmail.com', 'janio.silva@gmail.com']
    assert evento_serializado.data['local'] == 'Google Meet'
    assert evento_serializado.data['descricao'] == 'Call de alinhamento dos novos módulos do curso'
