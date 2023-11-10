from django.db import models
import uuid


class ReservationStatus(models.TextChoices):
    CONFIRMADO = 'confirmado'
    CANCELADA = 'cancelada'


class Reservation(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    checkin_date = models.DateTimeField()
    checkout_date = models.DateTimeField()
    status = models.CharField(max_length=10, choices=ReservationStatus.choices, default=ReservationStatus.CONFIRMADO)
