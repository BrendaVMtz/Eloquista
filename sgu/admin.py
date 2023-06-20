from django.contrib import admin
from .models import alumno,cuidador,alumno_cuidador,usuario,padre,salud,profesor

# Register your models here.
admin.site.register(usuario)
admin.site.register(alumno)
admin.site.register(cuidador)
admin.site.register(padre)
admin.site.register(salud)
admin.site.register(profesor)
admin.site.register(alumno_cuidador)