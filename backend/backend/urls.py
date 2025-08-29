from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Importamos los viewsets
from estudiantes.views import (
    EstudianteViewSet,
    EstudianteListView,
    EstudianteDetailView,
    EstudianteCreateView,
    EstudianteUpdateView,
    EstudianteDeleteView,
)

# Asistencias
from asistencia.views import (
    AsistenciaViewSet,
    AsistenciaListView,
    AsistenciaDetailView,
    AsistenciaCreateView,
    AsistenciaUpdateView,
    AsistenciaDeleteView,
)
# -------- API con DRF --------
router = DefaultRouter()
router.register(r"estudiantes", EstudianteViewSet, basename="estudiante")
router.register(r"asistencias", AsistenciaViewSet, basename="asistencia")

urlpatterns = [
    path("admin/", admin.site.urls),

    # Endpoints API
    path("api/", include(router.urls)),

    # -------- Vistas HTML Estudiantes --------
    path("estudiantes/", EstudianteListView.as_view(), name="estudiante_list"),
    path("estudiantes/<int:pk>/", EstudianteDetailView.as_view(), name="estudiante_detail"),
    path("estudiantes/crear/", EstudianteCreateView.as_view(), name="estudiante_create"),
    path("estudiantes/<int:pk>/editar/", EstudianteUpdateView.as_view(), name="estudiante_update"),
    path("estudiantes/<int:pk>/eliminar/", EstudianteDeleteView.as_view(), name="estudiante_delete"),

    # -------- Vistas HTML Asistencias --------
    path("asistencias/", AsistenciaListView.as_view(), name="asistencia_list"),
    path("asistencias/<int:pk>/", AsistenciaDetailView.as_view(), name="asistencia_detail"),
    path("asistencias/crear/", AsistenciaCreateView.as_view(), name="asistencia_create"),
    path("asistencias/<int:pk>/editar/", AsistenciaUpdateView.as_view(), name="asistencia_update"),
    path("asistencias/<int:pk>/eliminar/", AsistenciaDeleteView.as_view(), name="asistencia_delete"),
]