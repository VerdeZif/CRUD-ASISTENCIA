from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    EstudianteViewSet,
    EstudianteListView,
    EstudianteDetailView,
    EstudianteCreateView,
    EstudianteUpdateView,
    EstudianteDeleteView,
)

# -------- API con DRF --------
router = DefaultRouter()
router.register(r"api/estudiantes", EstudianteViewSet)

# -------- Vistas Django (HTML) --------
urlpatterns = [
    path("estudiantes/", EstudianteListView.as_view(), name="estudiante_list"),
    path("estudiantes/<int:pk>/", EstudianteDetailView.as_view(), name="estudiante_detail"),
    path("estudiantes/crear/", EstudianteCreateView.as_view(), name="estudiante_create"),
    path("estudiantes/<int:pk>/editar/", EstudianteUpdateView.as_view(), name="estudiante_update"),
    path("estudiantes/<int:pk>/eliminar/", EstudianteDeleteView.as_view(), name="estudiante_delete"),

    # API
    path("", include(router.urls)),
]