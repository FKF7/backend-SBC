
from rest_framework import serializers
# from django.db import IntegrityError
# from rest_framework.exceptions import ValidationError

from .models import Request

from users.serializers import UserSerializer

class RequestSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Request
        fields = "__all__"

    event_uuid = serializers.ReadOnlyField(source="event.uuid")

    def create(self, validated_data):
        event = validated_data.pop("event")
        user = self.context["request"].user
        
        return Request.objects.create(user=user, event=event, **validated_data)

        # try:
        #     return super().create(validated_data)
        # except IntegrityError:
        #     raise ValidationError(
        #         {"detail": "Você já possui uma solicitação para este evento."}
        #     )