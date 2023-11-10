from django.db import models
import uuid


class Payments(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
