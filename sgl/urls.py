from django.urls import path
from . import views

urlpatterns = [
    path('',views.examen),
    path('resultado',views.resultado, name = 'resultado'),

]