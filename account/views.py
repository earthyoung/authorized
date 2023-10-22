from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import *

from authorized.account.serializers import *


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class HouseViewSet(viewsets.ModelViewSet):
    serializer_class = HouseSerializer
    permission_classes = [IsAuthenticated]


class OwnershipViewSet(viewsets.ModelViewSet):
    serializer_class = OwnershipSerializer
    permission_classes = [IsAuthenticated]


class AuthorityViewSet(viewsets.ModelViewSet):
    serializer_class = AuthoritySerializer
    permission_classes = [IsAuthenticated]


class RecordViewSet(viewsets.ModelViewSet):
    serializer_class = RecordSerializer
    permission_classes = [IsAuthenticated]
