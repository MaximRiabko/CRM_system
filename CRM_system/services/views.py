from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy

from .forms import ServiceCreationForm, AdvertisingСompanyCreationForm
from .models import Service, AdvertisingСompany

class AdvertisingСompanyCreateView(CreateView):
    form_class = AdvertisingСompanyCreationForm
    template_name = "service/advertisingcompany_create.html"
    success_url = reverse_lazy("service:company_list")

class AdvertisingСompanyListView(ListView):
    model = AdvertisingСompany
    template_name = "service/advertisingcompany_list.html"
    context_object_name = 'company'

class AdvertisingСompanyDetailView(DetailView):
    model = AdvertisingСompany
    template_name = "service/advertisingcompany_detail.html"
    context_object_name = 'detail'

class AdvertisingСompanyUpdateView(UpdateView):
    model = AdvertisingСompany
    template_name = "service/advertisingcompany_update.html"
    form_class = ServiceCreationForm
    context_object_name = 'company'

class AdvertisingСompanyDeleteView(DeleteView):
    model = AdvertisingСompany
    template_name = "service/advertisingcompany_delete.html"
    success_url = reverse_lazy("service:company_list")


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

