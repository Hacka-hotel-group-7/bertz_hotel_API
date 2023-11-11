from django.db import models
import uuid


class HotelImage(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    image = models.TextField()
