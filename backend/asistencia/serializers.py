from rest_framework import serializers
from .models import Asistencia
from estudiantes.models import Estudiante


class AsistenciaSerializer(serializers.ModelSerializer):
    """
    Serializer básico para crear y actualizar asistencias.
    Solo usa el ID del estudiante.
    """

    class Meta:
        model = Asistencia
        fields = ["id", "estudiante", "fecha", "presente"]
        extra_kwargs = {
            "estudiante": {"required": True},
            "fecha": {"required": True},
        }

    def validate(self, data):
        """
        Evita duplicados: un estudiante no puede tener 2 asistencias
        para la misma fecha.
        """
        estudiante = data.get("estudiante")
        fecha = data.get("fecha")

        qs = Asistencia.objects.filter(estudiante=estudiante, fecha=fecha)

        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)

        if qs.exists():
            raise serializers.ValidationError(
                {"non_field_errors": ["Ya existe un registro de asistencia para este estudiante en esta fecha."]}
            )

        return data


class AsistenciaDetailSerializer(serializers.ModelSerializer):
    """
    Serializer detallado que muestra info del estudiante.
    """
    estudiante = serializers.SerializerMethodField()

    class Meta:
        model = Asistencia
        fields = ["id", "estudiante", "fecha", "presente"]

    def get_estudiante(self, obj):
        return {
            "id": obj.estudiante.id,
            "nombre": obj.estudiante.nombre,
            "apellido": obj.estudiante.apellido,
            "dni": obj.estudiante.dni,
            "matricula": obj.estudiante.matricula,
        }
