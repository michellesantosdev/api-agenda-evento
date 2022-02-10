from rest_framework.serializers import ModelSerializer

from agenda_evento.api.models import Evento


class EventSerializer(ModelSerializer):

    class Meta:
        model = Evento
        fields = '__all__'
