from django.urls import path
from . import views

urlpatterns = [
    path('',views.seleccionarPerfil),
    path('padre/',views.parent_signup),
    path('profesor/',views.teacher_signup),
    #path('login/',views.login),
    #path('profile/<str:username>',views.profile)
]