from django.urls import path
from . import views

urlpatterns = [
    path('sel_perfil/',views.seleccionPerfil),
    path('signup/',views.signup),
    path('login/',views.login),
    path('profile/<str:username>',views.profile)
]