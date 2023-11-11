from django.db import models
import uuid


class StatusChoices(models.IntegerChoices):
    THREE = 3
    FOUR = 4
    FIVE = 5


class Hotel(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    status = models.IntegerField(choices=StatusChoices.choices, default=StatusChoices.THREE)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=120)
    phone = models.CharField(max_length=12)
    description = models.TextField()
    services = models.ManyToManyField('services.Service', related_name='hotels', null=True)
    reviews = models.ManyToManyField('reviews.Review', related_name='hotels', null=True)
    promotions = models.ManyToManyField('promotions.Promotion', related_name='hotels', null=True)
