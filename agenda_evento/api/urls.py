from django.urls import path, include
from rest_framework_nested import routers

from agenda_evento.api.views import EventoViews


rota_evento = routers.DefaultRouter(trailing_slash=False)
rota_evento.register('eventos', EventoViews, basename='EventoViews')


app_name = 'api'


urlpatterns = (
    path('', include(rota_evento.urls)),
)
