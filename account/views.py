from django.shortcuts import render
from rest_framework import viewsets, views
from rest_framework.permissions import *
from django.http.response import *

from account.serializers import *
from account.models import *


# Create your views here.
class HealthViewSet(views.APIView):

    def get(self, request):
        return JsonResponse({"status": True})


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return User.objects.all()


class HouseViewSet(viewsets.ModelViewSet):
    serializer_class = HouseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return House.objects.all()


class OwnershipViewSet(viewsets.ModelViewSet):
    serializer_class = OwnershipSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Ownership.objects.all()


class AuthorityViewSet(viewsets.ModelViewSet):
    serializer_class = AuthoritySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Authority.objects.all()


class RecordViewSet(viewsets.ModelViewSet):
    serializer_class = RecordSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Record.objects.all()
