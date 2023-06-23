from django.contrib import admin
from .models import usuario,Tarea,Profesor

# Register your models here.

admin.site.register(usuario)
admin.site.register(Tarea)
admin.site.register(Profesor)