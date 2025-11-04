from django.db import models
from django.conf import settings

class Constants():
    EMAILS_FILE_PATH = f"{settings.BASE_DIR}/core/data/emails.txt"

class RequestStatus(models.IntegerChoices):
    PENDING = 1, "Pending"
    APPROVED = 2, "Approved"
    REJECTED = 3, "Rejected"
    EXPIRED = 4, "Expired"