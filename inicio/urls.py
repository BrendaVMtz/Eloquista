from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('acerca/', views.acerca),
    path('contacto/', views.contacto)
]