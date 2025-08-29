import pytest
from datetime import date
from estudiantes.models import Estudiante
from asistencia.models import Asistencia
from django.db import IntegrityError

@pytest.fixture
def estudiante(db):
    return Estudiante.objects.create(
        nombre="Juan",
        apellido="Pérez",
        dni="12345678",
        correo="juan.perez@example.com",
        matricula="A2025-01"
    )


@pytest.mark.django_db
def test_crear_asistencia(estudiante):
    asistencia = Asistencia.objects.create(
        estudiante=estudiante,
        fecha=date.today(),
        presente=True
    )
    assert asistencia.id is not None
    assert "Presente" in str(asistencia)


@pytest.mark.django_db
def test_asistencia_unica_por_fecha(estudiante):
    fecha = date(2025, 8, 28)
    Asistencia.objects.create(estudiante=estudiante, fecha=fecha, presente=True)
    with pytest.raises(IntegrityError):
        # Intentar duplicar asistencia para mismo estudiante y fecha
        Asistencia.objects.create(estudiante=estudiante, fecha=fecha, presente=False)


@pytest.mark.django_db
def test_asistencia_por_defecto_ausente(estudiante):
    asistencia = Asistencia.objects.create(
        estudiante=estudiante,
        fecha=date.today()
    )
    assert asistencia.presente is False
    assert "Ausente" in str(asistencia)


@pytest.mark.django_db
def test_relacion_asistencias_estudiante(estudiante):
    Asistencia.objects.create(estudiante=estudiante, fecha=date(2025, 8, 27), presente=True)
    Asistencia.objects.create(estudiante=estudiante, fecha=date(2025, 8, 28), presente=False)

    asistencias = estudiante.asistencias.all()
    assert asistencias.count() == 2
    # Verifica que ordering funciona (la más reciente primero)
    assert asistencias.first().fecha == date(2025, 8, 28)