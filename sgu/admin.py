from django.contrib import admin
from .models import usuario,profesor,padre,salud

# Register your models here.

admin.site.register(usuario)
admin.site.register(profesor)
admin.site.register(padre)
admin.site.register(salud)