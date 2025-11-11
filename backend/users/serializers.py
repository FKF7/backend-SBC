from rest_framework import serializers
from .models import User
from . import validators

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["cpf", "name", "email", "birth_date", "password", "created_at"]
        read_only_fields = ["id", "created_at"]
    
    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)   # ← gera hash + salt
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        for k, v in validated_data.items():
            setattr(instance, k, v)
        if password:
            instance.set_password(password)
        instance.save()
        return instance

    def validate_email(self, email):
        if validators.isEmailValid(email):
            return email
        else:
            raise serializers.ValidationError("Este e-mail não está autorizado.")
        
