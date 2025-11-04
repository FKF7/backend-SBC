from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["cpf", "name", "email", "birth_date", "created_at"]
        read_only_fields = ["id", "created_at"]
