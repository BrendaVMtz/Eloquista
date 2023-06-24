from django.shortcuts import render, redirect
from .models import Pregunta, Opcion, RespuestaUsuario, Calificacion
from django.contrib import messages

def examen(request):
    if request.method == 'POST':
        usuario = request.user
        preguntas = Pregunta.objects.all()
        total_preguntas = preguntas.count()
        puntaje = 0

        for pregunta in preguntas:
            opcion_seleccionada = request.POST.get(f'opcion_{pregunta.id}')

            if opcion_seleccionada:
                opcion = Opcion.objects.get(id=opcion_seleccionada)
                respuesta_usuario = RespuestaUsuario(usuario=usuario, pregunta=pregunta, opcion=opcion)
                respuesta_usuario.save()

                if opcion.es_correcta:
                    puntaje += 1

        calificacion = int((puntaje / total_preguntas) * 100)
        calificacion_usuario = Calificacion(usuario=usuario, calificacion=calificacion)
        calificacion_usuario.save()

        messages.success(request, 'Examen completado. Tu calificación se ha guardado.')
        return redirect('resultado')

    preguntas = Pregunta.objects.all()
    opciones = Opcion.objects.all()
    context = {
        'preguntas': preguntas,
        'opciones': opciones
    }
    return render(request, 'examen.html', context)

def resultado(request):
    usuario = request.user
    calificacion = Calificacion.objects.get(usuario=usuario)

    context = {
        'calificacion': calificacion
    }
    return render(request, 'resultado.html', context)


# from django.shortcuts import render
# from django.http import HttpResponse
# from django.shortcuts import get_object_or_404

# def home(request):
#         return HttpResponse("<h2>Selecciona tu perfil</h2>")

# def leccion(request):
#         return HttpResponse("<h2>Registrarse</h2>")
