from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import status

from agenda_evento.api.models import Evento


class EventoViews(GenericViewSet):

    def create(self, request):
        response_dados = {
            'mensagem': 'Dados recebidos com sucesso',
            'dados': request.data
        }

        return Response(response_dados, status.HTTP_201_CREATED)

    def list(self, request):
        todos_eventos = Evento.objects.all()
        return Response(todos_eventos, status.HTTP_200_OK)
