from rest_framework import viewsets, permissions
from .models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-email")
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny] # pode precisar mudar a permissão

@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def me(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)