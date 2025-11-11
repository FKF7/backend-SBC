from django.db import models
from localflavor.br.models import BRCPFField
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, cpf, email, password=None, **extra):
        if not cpf:
            raise ValueError("CPF obrigatório")
        email = self.normalize_email(email)
        user = self.model(cpf=cpf, email=email, **extra)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, cpf, email, password=None, **extra):
        extra.setdefault("is_staff", True)
        extra.setdefault("is_superuser", True)
        return self.create_user(cpf, email, password, **extra)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(primary_key=True)
    name = models.CharField(max_length=100)
    cpf = BRCPFField(unique=True)
    birth_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["cpf", "name", "birth_date"]

    def __str__(self):
        return self.name

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
