from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os

User = get_user_model()

class Command(BaseCommand):
    help = "Cria um superusuário automaticamente ao subir o Docker"

    def handle(self, *args, **kwargs):
        email = os.getenv("DJANGO_SUPERUSER_EMAIL")
        name = os.getenv("DJANGO_SUPERUSER_NAME")
        password = os.getenv("DJANGO_SUPERUSER_PASSWORD")
        birth_date = os.getenv("DJANGO_SUPERUSER_BIRTHDATE")

        if not email or not password or not name:
            self.stdout.write(self.style.WARNING(
                "Variáveis DJANGO_SUPERUSER_EMAIL e DJANGO_SUPERUSER_PASSWORD não definidas. Pulando criação."
            ))
            return

        if User.objects.filter(email=email).exists():
            self.stdout.write(self.style.SUCCESS(
                f"Superusuário '{email}' já existe."
            ))
            return

        self.stdout.write("Criando superusuário...")

        User.objects.create_superuser(
            email=email,
            name=name,
            password=password,
            birth_date=birth_date
        )

        self.stdout.write(self.style.SUCCESS(
            f"Superusuário '{email}' criado com sucesso!"
        ))
