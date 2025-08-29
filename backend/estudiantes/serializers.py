from rest_framework import serializers
from .models import Estudiante

class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = [
            'id',
            'nombre',
            'apellido',
            'dni',
            'correo',
            'matricula',
        ]
        extra_kwargs = {
            'dni': {
                'error_messages': {
                    'unique': "Este DNI ya está registrado."
                }
            },
            'correo': {
                'error_messages': {
                    'unique': "Este correo ya está registrado."
                }
            },
            'matricula': {
                'error_messages': {
                    'unique': "Esta matrícula ya está registrada."
                }
            },
        }