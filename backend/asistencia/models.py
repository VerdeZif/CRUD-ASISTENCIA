from django.db import models
from estudiantes.models import Estudiante

class Asistencia(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    fecha = models.DateField()
    presente = models.BooleanField(default=False)

    def __str__(self):
        return f"Asistencia de {self.estudiante} en {self.fecha}"
