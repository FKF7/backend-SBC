from django.db import models
from users.models import User
from core.constants import Roles
import uuid

# Create your models here.

class Place(models.Model):
    name = models.CharField(max_length=60)
    street = models.CharField(max_length=100)
    complement = models.CharField(max_length=10, blank=True, null=True)
    neighbourhood = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=60)
    state = models.CharField(max_length=2)
    country = models.CharField(max_length=20)

class Event(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=60)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    confirmation_limit_date = models.DateTimeField()
    description = models.TextField()
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name="events"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User,
        related_name="created_by_user",
        on_delete=models.DO_NOTHING
    )

    def __str__(self):
        return self.name
    
class RoleCost(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="role_costs")
    role = models.IntegerField(choices=Roles.choices)
    
    individual = models.DecimalField(max_digits=10, decimal_places=2)
    double = models.DecimalField(max_digits=10, decimal_places=2)
    guest = models.DecimalField(max_digits=10, decimal_places=2)
    days_covered = models.IntegerField(default=0)

    class Meta:
        unique_together = ("event", "role")

    def __str__(self):
        return f"{self.role} ({self.event.name})"

