import datetime
import factory

from agenda_evento.api.models import Evento


class EventFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Evento

    titulo = 'Call para Alinhar'
    data = datetime.date.today()
    horario_inicio = '13:00:00'
    horario_fim = '13:30:00'
    convidados = ['israel.silva@gmail.com', 'janio.silva@gmail.com']
    local = 'Google Meet'
    descricao = 'Call de alinhamento dos novos módulos do curso'
