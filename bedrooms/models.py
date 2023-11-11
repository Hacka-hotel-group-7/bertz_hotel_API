from django.db import models
import uuid


class RoomStatus(models.TextChoices):
    LIMPO = 'limpo'
    OCUPADO = 'ocupado'
    MANUTENCAO = 'manutenção'
    DISPONIVEL = 'disponível'


class Bedroom(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    status = models.CharField(max_length=10, choices=RoomStatus.choices, default=RoomStatus.DISPONIVEL)
    room_type = models.CharField(max_length=20)
    bed_number = models.IntegerField(default=2)
    price = models.IntegerField()
    image = models.TextField()
