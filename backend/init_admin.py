import os
from django.conf import settings
from django.contrib.auth import get_user_model
from dotenv import load_dotenv

# Carrega variáveis do .env
ENV_PATH = os.path.join(settings.BASE_DIR, ".env")
load_dotenv(ENV_PATH)

def run():
    User = get_user_model()

    admin_name = os.getenv("ADMIN_NAME")
    admin_email = os.getenv("ADMIN_EMAIL")
    admin_password = os.getenv("ADMIN_PASSWORD")
    print

    if not admin_email or not admin_password or not admin_name:
        print("Arquivo .env incompleto")
        return

    if not User.objects.filter(email=admin_email).exists():
        print("Criando usuário admin inicial...")

        User.objects.create_superuser(
            name=admin_name,
            email=admin_email,
            password=admin_password,
        )

        print("Administrador criado com sucesso.")
    else:
        print("Superusuário já existe. Nada a fazer.")
