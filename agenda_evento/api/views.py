from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404

from agenda_evento.api.models import Evento
from agenda_evento.api.serializers import EventSerializer


class EventoViews(GenericViewSet):
    serializer_class = EventSerializer
    queryset = Evento.objects.all()

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                "evento_id": serializer.data['id'],
                "message": f"Evento {serializer.data['titulo']} criado com sucesso."
            },
            status=status.HTTP_201_CREATED)

    def list(self, request):
        serializer = self.get_serializer(self.queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        event = get_object_or_404(self.queryset, pk=pk)
        serializer = self.get_serializer(event)

        return Response(serializer.data)

    def update(self, request, pk=None):
        evento = get_object_or_404(self.queryset, pk=pk)
        serializer = self.get_serializer(evento, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def destroy(self, request, pk=None):
        evento = get_object_or_404(self.queryset, pk=pk)
        evento.delete()
        data_response = {'id': pk, 'message': 'Evento removido com sucesso.'}
        return Response(data=data_response, status=status.HTTP_201_CREATED)

