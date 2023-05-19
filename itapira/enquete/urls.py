from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('felipe', views.caneta, name='caneta'),
    path("<int:questao_id>/", views.detalhe, name="detail"),
    # ex: /enquete/5/
    path("<int:questao_id>/resultados/", views.resultados, name="results"),
    # ex: /enquete/5/resultados/
    path("<int:questao_id>/voto/", views.voto, name="voto"),
    # ex: /enquete/5/voto/
]