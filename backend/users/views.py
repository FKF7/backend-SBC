from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import User
from .serializers import UserSerializer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-cpf")
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny] # pode precisar mudar a permissão