from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework import viewsets
from .models import Estudiante
from .serializers import EstudianteSerializer
from .forms import EstudianteForm


# -------- API con DRF --------
class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer


# -------- Vistas Django (HTML) --------

class EstudianteListView(ListView):
    model = Estudiante
    template_name = "estudiantes/estudiante_list.html"
    context_object_name = "estudiantes"
    ordering = ["apellido", "nombre"]


class EstudianteDetailView(DetailView):
    model = Estudiante
    template_name = "estudiantes/estudiante_detail.html"
    context_object_name = "estudiante"


class EstudianteCreateView(CreateView):
    model = Estudiante
    form_class = EstudianteForm
    template_name = "estudiantes/estudiante_form.html"
    success_url = reverse_lazy("estudiante_list")


class EstudianteUpdateView(UpdateView):
    model = Estudiante
    form_class = EstudianteForm
    template_name = "estudiantes/estudiante_form.html"
    success_url = reverse_lazy("estudiante_list")


class EstudianteDeleteView(DeleteView):
    model = Estudiante
    template_name = "estudiantes/estudiante_confirm_delete.html"
    success_url = reverse_lazy("estudiante_list")