from django.db import models

# Create your models here.
class Clase(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    video_url = models.URLField()
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Material(models.Model):
    id = models.AutoField(primary_key=True)
    clase = models.ForeignKey(Clase, on_delete=models.CASCADE, related_name='materiales')
    titulo = models.CharField(max_length=200)
    archivo = models.FileField(upload_to='materiales/')

    def __str__(self):
        return self.titulo

class Tarea(models.Model):
    id = models.AutoField(primary_key=True)
    clase = models.ForeignKey(Clase, on_delete=models.CASCADE, related_name='tareas')
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_limite = models.DateField()

    def __str__(self):
        return self.titulo

class Retroalimentacion(models.Model):
    id = models.AutoField(primary_key=True)
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE, related_name='retroalimentaciones')
    nombre_estudiante = models.CharField(max_length=100)
    comentario = models.TextField()

    def __str__(self):
        return f"Retroalimentación de {self.nombre_estudiante}"
