from django.db import models
from users.models import User
from events.models import Event
from core.constants import RequestStatus, Roles, TravelTime, RoomType
import uuid

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

    phone_number = models.CharField(max_length=14 , blank=True, default="")
    institution = models.CharField(max_length=80, null=True, blank=True)
    role = models.IntegerField(choices=Roles.choices)
    room_type = models.IntegerField(choices=RoomType.choices)
    people_count = models.IntegerField(default=1)
    checkin_date = models.DateField()
    checkout_date = models.DateField() 
    special_needs = models.TextField(blank=True, null=True)

    origin_city = models.CharField(max_length=60, blank=True, null=True)
    origin_state = models.CharField(max_length=2, blank=True, null=True)
    origin_airport = models.CharField(max_length=60, blank=True, null=True)
    departure_date = models.DateField(null=True, blank=True)
    departure_preferred_time = models.IntegerField(choices=TravelTime.choices, blank=True, null=True)
    return_date = models.DateField(null=True, blank=True)
    return_preferred_time = models.IntegerField(choices=TravelTime.choices, blank=True, null=True)
    
    expected_payment = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    value_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
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