from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import status


class EventoViews(GenericViewSet):

    def create(self, request):
        response_dados = {
            'mensagem': 'Dados recebidos com sucesso',
            'dados': request.data
        }

        return Response(response_dados, status.HTTP_201_CREATED)

    def list(self, request):
        response_evento = [
            {
                "titulo": "Call de Alinhamento",
                "data": "09/12/2021",
                "horario_inicio": "16:40",
                "horario_fim": "17:00",
                "convidados": [
                    "janiojs@icloud.com"
                ],
                "local": "https://meet.google.com/rbr-hhfr-mnt",
                "descricao": "Call para alinhar próximos módulos do curso"
            }
        ]
        return Response(response_evento, status.HTTP_200_OK)
