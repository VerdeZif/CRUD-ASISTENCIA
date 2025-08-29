from django import forms
from .models import Asistencia


class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = ["estudiante", "fecha", "presente"]

        widgets = {
            "estudiante": forms.Select(attrs={"class": "form-control"}),
            "fecha": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "presente": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }

        labels = {
            "estudiante": "Estudiante",
            "fecha": "Fecha de asistencia",
            "presente": "¿Asistió?",
        }