from django.urls import path
from . import views

urlpatterns = [
    path('leccion/<int:examen_id>/', views.leccion, name='leccion'),
    path('resultado/', views.resultado, name='resultado'),
]