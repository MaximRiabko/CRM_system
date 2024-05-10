from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy

from .forms import RegisterCreationForm

class ProfileUser(TemplateView):
    template_name = "users/about_me.html"

class RegisterUser(CreateView):
    form_class = RegisterCreationForm
    template_name = "users/register.html"
    success_url = reverse_lazy("users:about_me")

class LogoutView(LogoutView):
    next_page = reverse_lazy("users:login")


