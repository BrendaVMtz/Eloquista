from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('acerca/', views.acerca),
    path('contacto/', views.contacto)
]