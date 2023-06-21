from django.urls import path
from . import views

urlpatterns = [
    path('',views.registro)
    #path('login/',views.login),
    #path('profile/<str:username>',views.profile)
]