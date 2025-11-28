from rest_framework import serializers
from .models import Event, Place, RoleCost

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = "__all__"

class RoleCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleCost
        fields = ["role", "individual", "double", "guest", "days_covered"]
        
class EventSerializer(serializers.ModelSerializer):
    place = PlaceSerializer()
    role_costs = RoleCostSerializer(many=True)

    class Meta:
        model = Event
        fields = [
            "uuid",
            "name",
            "start_date",
            "end_date",
            "confirmation_limit_date",
            "description",
            "place",
            "role_costs",
            "created_at",
            "created_by",
        ]
        read_only_fields = ("uuid", "created_at", "created_by")
        
    def create(self, validated_data):
        place_data = validated_data.pop("place")
        role_costs_data = validated_data.pop("role_costs")
        print(role_costs_data)

        place = Place.objects.create(**place_data)

        event = Event.objects.create(place=place, **validated_data)

        for role_cost in role_costs_data:
            RoleCost.objects.create(event=event, **role_cost)

        return event
    
    def update(self, instance, validated_data):
        place_data = validated_data.pop("place", None)
        role_costs_data = validated_data.pop("role_costs", None)

        # Atualiza dados simples
        for key, value in validated_data.items():
            setattr(instance, key, value)

        if place_data:
            for key, value in place_data.items():
                setattr(instance.place, key, value)
            instance.place.save()
        
        if role_costs_data:
            instance.role_costs.all().delete()
            for rc in role_costs_data:
                RoleCost.objects.create(event=instance, **rc)

        instance.save()
        return instance
    
class EventPublicSerializer(serializers.ModelSerializer):
    place = PlaceSerializer()
    role_costs = RoleCostSerializer(many=True)

    class Meta:
        model = Event
        fields = "__all__"

