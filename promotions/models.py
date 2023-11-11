from django.db import models
import uuid


class Promotion(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=30)
    discount_amount = models.IntegerField()
