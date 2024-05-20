from django.urls import path
from .views import (
    ServiceCreateView,
    ServiceListView,
    ServiceDetailView,
    ServiceUpdateView,
    ServiceDeleteView,
)


app_name = "service"

urlpatterns = [
    path("create/", ServiceCreateView.as_view(), name="create_service"),
    path("", ServiceListView.as_view(), name="list_service"),
    path("detail/<int:pk>", ServiceDetailView.as_view(), name="detail_service"),
    path("update/<int:pk>", ServiceUpdateView.as_view(), name="update_service"),
    path("delete/<int:pk>", ServiceDeleteView.as_view(), name="delete_service"),
]