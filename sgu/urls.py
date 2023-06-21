from django.urls import path
from . import views

urlpatterns = [
    path('',views.registro),
    #path('registro_padre/',views.registro_padre),
    #path('registro_profesor/',views.registro_profesor),
    #path('registro_salud/',views.registro_profesor),
]