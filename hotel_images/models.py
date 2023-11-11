from django.db import models
import uuid


class HotelImages(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    image = models.TextField()
    hotel = models.ForeignKey('hotels.Hotel', on_delete=models.CASCADE, related_name='images')
