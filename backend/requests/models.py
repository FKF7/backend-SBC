from django.db import models
from users.models import User
from events.models import Event
from core.constants import RequestStatus
import uuid

# Create your models here.

class Request(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="requests",   # permite user.requests.all()
    )
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name="requests"
    )
    observations = models.TextField(blank=True, default="")
    status = models.IntegerField(choices=RequestStatus.choices, default=RequestStatus.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "event"],
                name="uniq_request_user_event",
            ),
        ]
        indexes = [
            models.Index(fields=["user", "event"]),
        ]

    def __str__(self):
        return self.name