from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import status

from agenda_evento.api.models import Evento
from agenda_evento.api.serializers import EventSerializer


class EventoViews(GenericViewSet):
    serializer_class = EventSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"message": f"Evento {serializer.data['titulo']} criado com sucesso."},
                        status=status.HTTP_201_CREATED)

    def list(self, request):
        listagem_eventos = Evento.objects.all()
        serializer = self.get_serializer(listagem_eventos, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
