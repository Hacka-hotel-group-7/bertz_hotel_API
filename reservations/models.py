from django.db import models
import uuid


class PaymentsMethods(models.TextChoices):
    DINHEIRO = 'Dinheiro'
    PIX = 'Pix'
    DEBITO = 'Débito'
    CREDITO = 'Crédito'


class ReservationStatus(models.TextChoices):
    CONFIRMADO = 'Confirmado'
    CANCELADA = 'Cancelada'


class Reservation(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    checkin_date = models.DateTimeField()
    checkout_date = models.DateTimeField(null=True, default=None)
    status = models.CharField(max_length=10, choices=ReservationStatus.choices, default=ReservationStatus.CONFIRMADO)
    paid = models.BooleanField(default=False)
    payments_methods = models.CharField(max_length=8, choices=PaymentsMethods.choices, null=True)
    total = models.FloatField()
    guest = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='reservations', null=True)
    bedroom = models.ForeignKey('bedrooms.Bedroom', on_delete=models.CASCADE, related_name='reservations')
