from django.urls import path
from . import views

urlpatterns = [
    path("health", views.HealthViewSet.as_view()),
    path("user", views.UserCreateViewSet.as_view()),
    path("user", views.UserViewSet.as_view()),
    path("house", views.HouseViewSet.as_view({"get": "list"})),
    path("ownership", views.OwnershipViewSet.as_view({"get": "list"})),
    path("authority", views.AuthorityViewSet.as_view({"get": "list"})),
    path("record", views.RecordViewSet.as_view({"get": "list"})),
    path("ownership/request", views.OwnershipRequestViewSet.as_view({"get": "list"})),
    path("authority/request", views.AuthorityRequestViewSet.as_view({"get": "list"})),
    path("google/login", views.GoogleLoginView.as_view()),
    path("google/callback", views.GoogleCallbackView.as_view()),
    path("google/login/finish", views.GoogleLoginFinishView.as_view()),
]
