from django.urls import path
from . import views

urlpatterns = [
    path('examen/<int:examen_id>/', views.examen, name='examen'),
    path('resultado/', views.resultado, name='resultado'),
]