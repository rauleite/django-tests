from django.shortcuts import render
from app.models import Cliente


def index(request):
    c = Cliente()
    r = c.nome = 'raul'
    return render(request, 'app/index.html', {'nome': c.nome})