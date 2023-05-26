from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    ultimas_questoes = Questao.objects.order_by("-data")[:5]
    saida = ", ".join([q.pergunta for q in ultimas_questoes])
    saida = ""
    for q in ultimas_questoes:
        linha = f"<p>q.pergunta</p>"
        saida.join(linha)
        
    return HttpResponse(saida)

def index(request):
    return HttpResponse("<h1>Olha, se você não me ama</h1><h2>Caneta azul, azul caneta</h2>")

def caneta(request):
    return HttpResponse("<h1>Caneta azul, azul caneta...</h1>")

def detalhe(request, questao_id):
    return HttpResponse("Você está olhando a questão %s." % questao_id)

def resultados(request, questao_id):
    response = "Você está olhando o resultado da questão %s."
    return HttpResponse(response % questao_id)

def voto(request, questao_id):
    return HttpResponse("Você está votando na questão %s." % questao_id)