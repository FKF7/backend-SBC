from django.db import models
from localflavor.br.models import BRCPFField

# Create your models here.

class User(models.Model):
    cpf = BRCPFField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    birth_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name