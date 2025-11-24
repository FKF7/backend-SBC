from django.db import models
from users.models import User

# Create your models here.

class Place(models.Model):
    name = models.CharField(max_length=40)
    street = models.CharField(max_length=100)
    complement = models.CharField(max_length=10)
    neighbourhood = models.CharField(max_length=30)
    city = models.CharField(max_length=60)
    state = models.CharField(max_length=2)
    country = models.CharField(max_length=20)

class Event(models.Model):
    name = models.CharField(max_length=60)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    place = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User,
        related_name="created_by_user",
        on_delete=models.DO_NOTHING
    )
    event = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name="events"
    )

    def __str__(self):
        return self.name
    
