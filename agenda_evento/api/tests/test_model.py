import pytest

from ..models import Evento


pytestmark = [pytest.mark.django_db]


def test_deve_criar_evento_base(evento):
    assert Evento.objects.count() == 1
    assert evento.titulo == 'Call para Alinhar'
    assert evento.data is not None
    assert evento.horario_inicio == '13:00:00'
    assert evento.horario_fim == '13:30:00'
    assert evento.convidados == ['israel.silva@gmail.com', 'janio.silva@gmail.com']
    assert evento.local == 'Google Meet'
    assert evento.descricao == 'Call de alinhamento dos novos módulos do curso'
