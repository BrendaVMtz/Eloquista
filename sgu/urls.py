from django.urls import path
from . import views

urlpatterns = [
    path('',views.seleccionPerfil),
    path('signup/',views.signup),
    path('login/',views.login),
]