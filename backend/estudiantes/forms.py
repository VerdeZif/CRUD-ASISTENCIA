from django import forms
from .models import Estudiante


class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ["nombre", "apellido", "dni", "correo", "matricula"]

        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ingrese nombre"}),
            "apellido": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ingrese apellido"}),
            "dni": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ejemplo: 87654321"}),
            "correo": forms.EmailInput(attrs={"class": "form-control", "placeholder": "ejemplo@correo.com"}),
            "matricula": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ejemplo: MAT-2025"}),
        }

        labels = {
            "nombre": "Nombre",
            "apellido": "Apellido",
            "dni": "DNI",
            "correo": "Correo Electrónico",
            "matricula": "Matrícula",
        }

        help_texts = {
            "dni": "Debe contener exactamente 8 dígitos numéricos.",
            "matricula": "Solo letras, números y guiones (ejemplo: MAT-2025).",
        }