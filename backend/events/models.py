from django.db import models
from users.models import User

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=60)
    date = models.DateTimeField()
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User,
        related_name="created_by_user",
        on_delete=models.DO_NOTHING
    )

    def __str__(self):
        return self.name