from rest_framework import serializers
from .models import User
from . import validators

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["cpf", "name", "email", "birth_date", "created_at"]
        read_only_fields = ["id", "created_at"]

    def validate_email(self, email):
        if validators.isEmailValid(email):
            return email
        else:
            raise serializers.ValidationError("Este e-mail não está autorizado.")
        
