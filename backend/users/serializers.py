from rest_framework import serializers
from .models import User
from core.constants import Constants

def is_email_whitelisted(email) -> bool:
    with open(Constants.EMAILS_FILE_PATH, "r") as file:
        data = file.readlines()
        for line in data:
            if email == line.strip():
                return True
        return False

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "name", "birth_date", "cpf", "passport_number", "passport_country", "password", "created_at"]
        read_only_fields = ["created_at"]
        extra_kwargs = {
            "password": {"write_only": True},
        }
    
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
        if not is_email_whitelisted(email):
            raise serializers.ValidationError("Este e-mail não está autorizado.")
        return email
    
    def validade_document(self, data):
        cpf_value = data.get("cpf")
        passport_number = data.get("passport_number")
        passport_country = data.get("passport_country")

        if not (cpf_value ^ (passport_number and passport_country)):
            raise serializers.ValidationError("Informação de documento incompleta ou inválida")