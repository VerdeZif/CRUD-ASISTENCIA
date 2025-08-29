from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework import viewsets
from .models import Asistencia
from .serializers import AsistenciaSerializer, AsistenciaDetailSerializer
from .forms import AsistenciaForm

# -------- API con DRF --------

class AsistenciaViewSet(viewsets.ModelViewSet):
    queryset = Asistencia.objects.select_related("estudiante").all()
    serializer_class = AsistenciaSerializer

    def get_serializer_class(self):
        """Usar serializer detallado para list/retrieve, básico para create/update"""
        if self.action in ["list", "retrieve"]:
            return AsistenciaDetailSerializer
        return AsistenciaSerializer


# -------- Vistas Django (HTML) --------

class AsistenciaListView(ListView):
    model = Asistencia
    template_name = "asistencias/asistencia_list.html"
    context_object_name = "asistencias"
    ordering = ["-fecha"]


class AsistenciaDetailView(DetailView):
    model = Asistencia
    template_name = "asistencias/asistencia_detail.html"
    context_object_name = "asistencia"


class AsistenciaCreateView(CreateView):
    model = Asistencia
    form_class = AsistenciaForm
    template_name = "asistencias/asistencia_form.html"
    success_url = reverse_lazy("asistencia_list")


class AsistenciaUpdateView(UpdateView):
    model = Asistencia
    form_class = AsistenciaForm
    template_name = "asistencias/asistencia_form.html"
    success_url = reverse_lazy("asistencia_list")


class AsistenciaDeleteView(DeleteView):
    model = Asistencia
    template_name = "asistencias/asistencia_confirm_delete.html"
    success_url = reverse_lazy("asistencia_list")