from django.urls import path
from . import views

urlpatterns = [
    path("health", views.HealthViewSet.as_view()),
    path("user", views.UserViewSet.as_view({"get": "list"})),
    path("house", views.HouseViewSet.as_view({"get": "list"})),
    path("ownership", views.OwnershipViewSet.as_view({"get": "list"})),
    path("authority", views.AuthorityViewSet.as_view({"get": "list"})),
    path("record", views.RecordViewSet.as_view({"get": "list"})),
    path("ownership/request", views.OwnershipRequestViewSet.as_view({"get": "list"})),
    path("authority/request", views.AuthorityRequestViewSet.as_view({"get": "list"})),
]
