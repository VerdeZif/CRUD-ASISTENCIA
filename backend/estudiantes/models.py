from django.db import models
from django.core.validators import RegexValidator

class Estudiante(models.Model):
    id = models.AutoField(primary_key=True)

    nombre = models.CharField(
        max_length=100,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$',
                message="El nombre solo puede contener letras y espacios"
            )
        ]
    )
    apellido = models.CharField(
        max_length=100,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$',
                message="El apellido solo puede contener letras y espacios"
            )
        ]
    )
    dni = models.CharField(
        max_length=8,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^\d{8}$',
                message="El DNI debe contener exactamente 8 dígitos numéricos"
            )
        ]
    )
    correo = models.EmailField(
        unique=True,
        error_messages={
            "unique": "Este correo ya está registrado."
        }
    )
    matricula = models.CharField(
        max_length=20,
        unique=True,
        default="TEMP-0000",
        validators=[
            RegexValidator(
                regex=r'^[A-Za-z0-9-]+$',
                message="La matrícula solo puede contener letras, números y guiones"
            )
        ]
    )

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.matricula}"