from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class UserRole(models.TextChoices):
    HOSPEDE = 'hospede'
    GENRENTE = 'gerente'
    STAFF = 'staff'


class DocumentType(models.TextChoices):
    RG = 'RG'
    CPF = 'CPF'
    PASSAPORTE = 'PASSAPORTE'
    OUTRO = 'OUTRO'


class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=120)
    username = models.EmailField(max_length=120, unique=True)
    password = models.CharField(max_length=255)
    country_code = models.CharField(max_length=4)
    contact_info = models.CharField(max_length=16, null=True)
    document_type = models.CharField(max_length=10, choices=DocumentType.choices, default=DocumentType.CPF)
    document_number = models.CharField(max_length=15, unique=True)
    role = models.CharField(max_length=7, choices=UserRole.choices, default=UserRole.HOSPEDE)
    is_superuser = models.BooleanField(default=False)
    reviews = models.ManyToManyField('reviews.Review', related_name='guests')
