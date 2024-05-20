from django.shortcuts import render
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy

from .forms import ServiceCreationForm
from .models import Service

class ServiceCreateView(CreateView):
    form_class = ServiceCreationForm
    template_name = "service/service_create.html"
    success_url = reverse_lazy("service:list_service")

class ServiceListView(ListView):
    model = Service
    template_name = "service/service_list.html"
    context_object_name = 'service'

class ServiceDetailView(DetailView):
    model = Service
    template_name = "service/service_detail.html"

class ServiceUpdateView(UpdateView):
    model = Service
    template_name = "service/service_update.html"
    form_class = ServiceCreationForm

class ServiceDeleteView(DeleteView):
    model = Service
    template_name = "service/service_delete.html"
    success_url = reverse_lazy("service:list_service")
