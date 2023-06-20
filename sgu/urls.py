from django.urls import path
from . import views

urlpatterns = [
    path('sel_perfil/',views.seleccionPerfil),
    path(' ',views.teacher_signup),
    path('TeacherSignUp/',views.parent_signup),
    path('login/',views.login),
    path('profile/<str:username>',views.profile)
]