from rest_framework import serializers
from .models import Asistencia

class AsistenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asistencia
        fields = '__all__'

    def validate(self, data):
        estudiante = data.get("estudiante")
        fecha = data.get("fecha")

        # Filtrar si ya existe ese estudiante en esa fecha
        qs = Asistencia.objects.filter(estudiante=estudiante, fecha=fecha)

        # Si estoy editando, excluir este mismo registro
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)

        if qs.exists():
            raise serializers.ValidationError(
                "Ya existe un registro de asistencia para este estudiante en esa fecha."
            )

        return data

