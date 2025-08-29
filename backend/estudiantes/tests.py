import pytest
from estudiantes.models import Estudiante
from django.core.exceptions import ValidationError

@pytest.mark.django_db
def test_crear_estudiante_valido():
    estudiante = Estudiante.objects.create(
        nombre="Juan",
        apellido="Pérez",
        dni="12345678",
        correo="juan.perez@example.com",
        matricula="A2025-01"
    )
    assert estudiante.id is not None
    assert str(estudiante) == "Juan Pérez - A2025-01"


@pytest.mark.django_db
def test_dni_invalido_largo():
    estudiante = Estudiante(
        nombre="Ana",
        apellido="Gómez",
        dni="123456789",  # 9 dígitos (inválido)
        correo="ana.gomez@example.com",
        matricula="A2025-02"
    )
    with pytest.raises(ValidationError):
        estudiante.full_clean()  # dispara validaciones


@pytest.mark.django_db
def test_nombre_invalido_con_numero():
    estudiante = Estudiante(
        nombre="Carlos123",  # inválido
        apellido="Ramírez",
        dni="87654321",
        correo="carlos.ramirez@example.com",
        matricula="A2025-03"
    )
    with pytest.raises(ValidationError):
        estudiante.full_clean()


@pytest.mark.django_db
def test_correo_unico():
    Estudiante.objects.create(
        nombre="Pedro",
        apellido="López",
        dni="11112222",
        correo="pedro@example.com",
        matricula="A2025-04"
    )
    with pytest.raises(Exception):  # IntegrityError o ValidationError
        Estudiante.objects.create(
            nombre="Pablo",
            apellido="López",
            dni="33334444",
            correo="pedro@example.com",  # correo duplicado
            matricula="A2025-05"
        )


@pytest.mark.django_db
def test_matricula_valida():
    estudiante = Estudiante(
        nombre="Lucía",
        apellido="Martínez",
        dni="55556666",
        correo="lucia@example.com",
        matricula="EST-001"  # válido por regex
    )
    estudiante.full_clean()