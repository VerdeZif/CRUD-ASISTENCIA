from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from estudiantes.views import EstudianteViewSet
from asistencia.views import AsistenciaViewSet

router = DefaultRouter()
router.register(r"estudiantes", EstudianteViewSet)
router.register(r"asistencias", AsistenciaViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),  # todas las rutas de API
]
