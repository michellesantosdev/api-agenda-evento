from django.http import HttpResponse


def home(requests):
    return HttpResponse('Oi, cliente LINDO')
