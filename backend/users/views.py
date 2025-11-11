from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-cpf")
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny] # pode precisar mudar a permissão

@api_view(["POST"])
@permission_classes([permissions.AllowAny])
def login_and_set_cookies(request):
    cpf = request.data.get("cpf")
    password = request.data.get("password")

    user = authenticate(request, cpf=cpf, password=password)
    if user is None:
        return Response({"detail": "CPF ou senha inválidos."}, status=400)

    refresh = RefreshToken.for_user(user)
    access_token = str(refresh.access_token)

    response = Response({"message": "Login bem-sucedido!"})
    # ↓ Cookies httpOnly (não acessíveis via JS)
    response.set_cookie(
        key="access",
        value=access_token,
        httponly=True,
        samesite="Lax",
        secure=False,  # True em produção HTTPS
        max_age=60 * 15,  # 15 minutos
    )
    response.set_cookie(
        key="refresh",
        value=str(refresh),
        httponly=True,
        samesite="Lax",
        secure=False,
        max_age=60 * 60 * 24 * 7,  # 7 dias
    )
    return response