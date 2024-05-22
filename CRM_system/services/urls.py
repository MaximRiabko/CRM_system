from django.urls import path
from .views import (
    ServiceCreateView,
    ServiceListView,
    ServiceDetailView,
    ServiceUpdateView,
    ServiceDeleteView,
    AdvertisingСompanyCreateView,
    AdvertisingСompanyListView,
    AdvertisingСompanyDetailView,
    AdvertisingСompanyUpdateView,
    AdvertisingСompanyDeleteView,
)


app_name = "service"

urlpatterns = [
    path("create/", ServiceCreateView.as_view(), name="create_service"),
    path("", ServiceListView.as_view(), name="list_service"),
    path("detail/<int:pk>", ServiceDetailView.as_view(), name="detail_service"),
    path("update/<int:pk>", ServiceUpdateView.as_view(), name="update_service"),
    path("delete/<int:pk>", ServiceDeleteView.as_view(), name="delete_service"),
    path("advertising_company/create/", AdvertisingСompanyCreateView.as_view(), name="company_create"),
    path("advertising_company/list/", AdvertisingСompanyListView.as_view(), name="company_list"),
    path("advertising_company/detail/<int:pk>", AdvertisingСompanyDetailView.as_view(), name="company_detail"),
    path("advertising_company/update/<int:pk>", AdvertisingСompanyUpdateView.as_view(), name="company_update"),
    path("advertising_company/delete/<int:pk>", AdvertisingСompanyDeleteView.as_view(), name="company_delete"),
]