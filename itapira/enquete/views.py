from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import Questao

# Create your views here.

def index(request):
    # selecionar na tabela questoes ultimos  5 objetos cadastrados
    ultimas_questoes = Questao.objects.order_by("data")[:5]
    # criamos um dicionario em python
    # (semelhante aos arrays associativos do php)
    # (ou aos arrays objetos literais do javascript)
    # (onde passamos essa variavel paraser utilizada no templete)
    context = {'ultimas_questoes': ultimas_questoes}
    return render(request, 'enquete/index.html', context)
    # retornar a função render, passando como argumentos
    # a requisição, otemplete queserá utilizado
    # e as variáveis de contextoque serão utilizadas dentro do templete

def caneta(request):
    return HttpResponse("<h1>Caneta Azul, Azul caneta...</h1>")


def detalhe(request, questao_id):
    try:
        question = Questao.objects.get(pk=questao_id)
    except Questao.DoesNotExist:
        raise Http404("Questão não existe")
    return render(repeat)


def resultados(request, questao_id):
    response = "Voce esta olhando o resultado da questao %s."
    return HttpResponse(response % questao_id)


def voto(request, questao_id):
    return HttpResponse("Voce esta votando na questao %s." % questao_id)