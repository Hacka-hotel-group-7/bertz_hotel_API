from django.db import models
import uuid


class Payments(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    classification = models.IntegerField()
    comments = models.TextField()
