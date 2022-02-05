from django.http import HttpResponse


def home(requests):
    return HttpResponse('OIE, cliente LINDO')
