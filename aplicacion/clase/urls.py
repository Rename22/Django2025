# URLS especificas de la aplicacion
from django.urls import path

from . import views

urlpatterns = [
    path('', views.inicio),  # Página de inicio

    


    # clase
    path('nuevaClase/', views.nuevaClase),  # Sin parámetro propietario_id  # Formulario para agregar nueva mascota
    path('listadoClase/', views.listadoClase),  # Listado de mascotas
    path('guardarClase/', views.guardarClase),  # Guardar nueva mascota
    path('editarClase/<clase_id>', views.editarClase), # Editar mascota
    path('eliminarClase/<clase_id>', views.eliminarClase), # Eliminar mascota
    path('procesarEdicionClase/', views.procesarEdicionClase),

    # Material
    path('nuevaMaterial/', views.nuevaMaterial),  # Formulario para agregar nuevo propietario
    path('listadoMaterial/', views.listadoMaterial),  # Listado de propietarios
    path('guardarMaterial/', views.guardarMaterial),  # Guardar nuevo propietario
    path('editarMaterial/<material_id>', views.editarMaterial), # Editar propietario
    path('eliminarMaterial/<material_id>', views.eliminarMaterial), # Eliminar propietario
    path('procesarEdicionMaterial/', views.procesarEdicionMaterial),   # Guardar el estudiante
    # Tarea
    path('nuevaTarea/', views.nuevaTarea),  # Formulario para agregar nuevo reporte
    path('listadoTarea/', views.listadoTarea),  # Listado de reportes
    path('guardarTarea/', views.guardarTarea),  # Guardar nuevo reporte
    path('editarTarea/<tarea_id>', views.editarTarea),  # Editar reporte
    path('procesarEdicionTarea/', views.procesarEdicionTarea),   # Guardar el estudiante
    path('eliminarTarea/<tarea_id>', views.eliminarTarea), # Eliminar reporte
       # Retroalimentacion
    path('nuevaRetroalimentacion/', views.nuevaRetroalimentacion),  # Formulario para agregar nuevo reporte
    path('listadoRetroalimentacion/', views.listadoRetroalimentacion),  # Listado de reportes
    path('guardarRetroalimentacion/', views.guardarRetroalimentacion),  # Guardar nuevo reporte
    path('editarRetroalimentacion/<retroalimentacion_id>', views.editarRetroalimentacion),  # Editar reporte
    path('procesarEdicionRetroalimentacion/', views.procesarEdicionRetroalimentacion),
    path('eliminarRetroalimentacion/<retroalimentacion_id>', views.eliminarRetroalimentacion), # Eliminar reporte
]