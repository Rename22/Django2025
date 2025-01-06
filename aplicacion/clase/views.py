from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Clase
from .models import Material
from .models import Tarea
from .models import Retroalimentacion

# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')


# Clases ---------------------------------------------------------------------------------------------

# Vista para mostrar el formulario de nueva Clase
def nuevaClase(request):
    return render(request, 'nuevaClase.html')

# Vista para mostrar la lista de Clases
def listadoClase(request):
    clasesBdd = Clase.objects.all()
    return render(request, 'listadoClase.html', {'clases': clasesBdd})

# Vista para guardar una nueva Clase
def guardarClase(request):
    titulo = request.POST['titulo']
    descripcion = request.POST['descripcion']
    video_url = request.POST['video_url']

    Clase.objects.create(
        titulo=titulo,
        descripcion=descripcion,
        video_url=video_url
    )
    messages.success(request, "Clase Guardada Exitosamente")
    return redirect('/listadoClase')

# Vista para eliminar una Clase
def eliminarClase(request, clase_id):
    claseEliminar = Clase.objects.get(id=clase_id)
    claseEliminar.delete()
    messages.success(request, "Clase Eliminada Exitosamente")
    return redirect('/listadoClase')

# Vista para editar una Clase
def editarClase(request, clase_id):
    claseEditar = Clase.objects.get(id=clase_id)
    return render(request, 'editarClase.html', {'clase': claseEditar})

# Vista para procesar la edición de una Clase
def procesarEdicionClase(request):
    clase = Clase.objects.get(id=request.POST['id'])
    clase.titulo = request.POST['titulo']
    clase.descripcion = request.POST['descripcion']
    clase.video_url = request.POST['video_url']

    clase.save()
    messages.success(request, "Clase Actualizada Exitosamente")
    return redirect('/listadoClase')

# Materiales ---------------------------------------------------------------------------------------------

# Vista para mostrar el formulario de nuevo Material
def nuevaMaterial(request):
    clases = Clase.objects.all()  # Obtener todas las clases
    return render(request, 'nuevaMaterial.html', {'clases': clases})

# Vista para mostrar la lista de Materiales
def listadoMaterial(request):
    materialesBdd = Material.objects.all()
    return render(request, 'listadoMaterial.html', {'materiales': materialesBdd})

# Vista para guardar un nuevo Material
def guardarMaterial(request):
    titulo = request.POST['titulo']
    archivo = request.FILES['archivo']
    clase_id = request.POST['clase']

    clase = Clase.objects.get(id=clase_id)

    # Guardar el material
    Material.objects.create(
        titulo=titulo,
        archivo=archivo,
        clase=clase
    )
    messages.success(request, "Material Guardado Exitosamente")
    return redirect('/listadoMaterial')


# Vista para eliminar un Material
def eliminarMaterial(request, material_id):
    materialEliminar = Material.objects.get(id=material_id)
    materialEliminar.delete()
    messages.success(request, "Material Eliminado Exitosamente")
    return redirect('/listadoMaterial')

# Vista para editar un Material
def editarMaterial(request, material_id):
    materialEditar = Material.objects.get(id=material_id)
    clases = Clase.objects.all()  # Obtener todas las clases
    return render(request, 'editarMaterial.html', {'material': materialEditar, 'clases': clases})

# Vista para procesar la edición de un Material
from django.core.exceptions import ObjectDoesNotExist

def procesarEdicionMaterial(request):
    try:
        material = Material.objects.get(id=request.POST['id'])
        material.titulo = request.POST['titulo']

        # Verificar si se envió un archivo
        if 'archivo' in request.FILES:
            material.archivo = request.FILES['archivo']

        material.clase = Clase.objects.get(id=request.POST['clase'])
        material.save()
        messages.success(request, "Material Actualizado Exitosamente")
    except ObjectDoesNotExist:
        messages.error(request, "Material o Clase no encontrado.")
    except Exception as e:
        messages.error(request, f"Ocurrió un error: {e}")
    return redirect('/listadoMaterial')


# Tareas ---------------------------------------------------------------------------------------------

# Vista para mostrar el formulario de nueva Tarea
def nuevaTarea(request):
    clases = Clase.objects.all()  # Obtener todas las clases
    return render(request, 'nuevaTarea.html', {'clases': clases})

# Vista para mostrar la lista de Tareas
def listadoTarea(request):
    tareasBdd = Tarea.objects.all()
    return render(request, 'listadoTarea.html', {'tareas': tareasBdd})

# Vista para guardar una nueva Tarea
def guardarTarea(request):
    titulo = request.POST['titulo']
    descripcion = request.POST['descripcion']
    fecha_limite = request.POST['fecha_limite']
    clase_id = request.POST['clase']

    clase = Clase.objects.get(id=clase_id)

    Tarea.objects.create(
        titulo=titulo,
        descripcion=descripcion,
        fecha_limite=fecha_limite,
        clase=clase
    )
    messages.success(request, "Tarea Guardada Exitosamente")
    return redirect('/listadoTarea')

# Vista para eliminar una Tarea
def eliminarTarea(request, tarea_id):
    tareaEliminar = Tarea.objects.get(id=tarea_id)
    tareaEliminar.delete()
    messages.success(request, "Tarea Eliminada Exitosamente")
    return redirect('/listadoTarea')

# Vista para editar una Tarea
def editarTarea(request, tarea_id):
    tareaEditar = Tarea.objects.get(id=tarea_id)
    clases = Clase.objects.all()  # Obtener todas las clases
    return render(request, 'editarTarea.html', {'tarea': tareaEditar, 'clases': clases})

# Vista para procesar la edición de una Tarea
def procesarEdicionTarea(request):
    tarea = Tarea.objects.get(id=request.POST['id'])
    tarea.titulo = request.POST['titulo']
    tarea.descripcion = request.POST['descripcion']
    tarea.fecha_limite = request.POST['fecha_limite']
    tarea.clase = Clase.objects.get(id=request.POST['clase'])

    tarea.save()
    messages.success(request, "Tarea Actualizada Exitosamente")
    return redirect('/listadoTarea')

# Retroalimentaciones -------------------------------------------------------------------------------------

# Vista para mostrar el formulario de nueva Retroalimentación
def nuevaRetroalimentacion(request):
    tareas = Tarea.objects.all()  # Obtener todas las tareas
    return render(request, 'nuevaRetroalimentacion.html', {'tareas': tareas})

# Vista para mostrar la lista de Retroalimentaciones
def listadoRetroalimentacion(request):
    retroalimentacionesBdd = Retroalimentacion.objects.all()
    return render(request, 'listadoRetroalimentacion.html', {'retroalimentaciones': retroalimentacionesBdd})

# Vista para guardar una nueva Retroalimentación
def guardarRetroalimentacion(request):
    nombre_estudiante = request.POST['nombre_estudiante']
    comentario = request.POST['comentario']
    tarea_id = request.POST['tarea']

    tarea = Tarea.objects.get(id=tarea_id)

    Retroalimentacion.objects.create(
        nombre_estudiante=nombre_estudiante,
        comentario=comentario,
        tarea=tarea
    )
    messages.success(request, "Retroalimentación Guardada Exitosamente")
    return redirect('/listadoRetroalimentacion')

# Vista para eliminar una Retroalimentación
def eliminarRetroalimentacion(request, retroalimentacion_id):
    retroalimentacionEliminar = Retroalimentacion.objects.get(id=retroalimentacion_id)
    retroalimentacionEliminar.delete()
    messages.success(request, "Retroalimentación Eliminada Exitosamente")
    return redirect('/listadoRetroalimentacion')

# Vista para editar una Retroalimentación
def editarRetroalimentacion(request, retroalimentacion_id):
    retroalimentacionEditar = Retroalimentacion.objects.get(id=retroalimentacion_id)
    tareas = Tarea.objects.all()  # Obtener todas las tareas
    return render(request, 'editarRetroalimentacion.html', {'retroalimentacion': retroalimentacionEditar, 'tareas': tareas})

# Vista para procesar la edición de una Retroalimentación
def procesarEdicionRetroalimentacion(request):
    retroalimentacion = Retroalimentacion.objects.get(id=request.POST['id'])
    retroalimentacion.nombre_estudiante = request.POST['nombre_estudiante']
    retroalimentacion.comentario = request.POST['comentario']
    retroalimentacion.tarea = Tarea.objects.get(id=request.POST['tarea'])

    retroalimentacion.save()
    messages.success(request, "Retroalimentación Actualizada Exitosamente")
    return redirect('/listadoRetroalimentacion')
