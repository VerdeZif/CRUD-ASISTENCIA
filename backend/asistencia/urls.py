from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    AsistenciaViewSet,
    AsistenciaListView,
    AsistenciaDetailView,
    AsistenciaCreateView,
    AsistenciaUpdateView,
    AsistenciaDeleteView,
)

# -------- API con DRF --------
router = DefaultRouter()
router.register(r"api/asistencias", AsistenciaViewSet, basename="asistencia")

# -------- Vistas Django (HTML) --------
urlpatterns = [
    # CRUD HTML
    path("", AsistenciaListView.as_view(), name="asistencia_list"),
    path("<int:pk>/", AsistenciaDetailView.as_view(), name="asistencia_detail"),
    path("crear/", AsistenciaCreateView.as_view(), name="asistencia_create"),
    path("<int:pk>/editar/", AsistenciaUpdateView.as_view(), name="asistencia_update"),
    path("<int:pk>/eliminar/", AsistenciaDeleteView.as_view(), name="asistencia_delete"),

    # API
    path("", include(router.urls)),
]