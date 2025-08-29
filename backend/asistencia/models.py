from django.db import models
from estudiantes.models import Estudiante


class Asistencia(models.Model):
    estudiante = models.ForeignKey(
        Estudiante,
        on_delete=models.CASCADE,
        related_name="asistencias"
    )
    fecha = models.DateField()
    presente = models.BooleanField(default=False)

    class Meta:
        unique_together = ("estudiante", "fecha")  # no permitir duplicados
        ordering = ["-fecha"]  # mostrar los más recientes primero

    def __str__(self):
        estado = "Presente" if self.presente else "Ausente"
        return f"{self.estudiante.nombre} {self.estudiante.apellido} - {self.fecha} ({estado})"