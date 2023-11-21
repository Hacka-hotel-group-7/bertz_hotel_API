from rest_framework import serializers
from .models import Hotel
from hotel_images.serializers import HotelImageSerializer
from bedrooms.serializers import BedroomSerializer
from services.serializers import ServiceSerializer


class HotelSerializer(serializers.ModelSerializer):
    images = HotelImageSerializer(read_only=True, many=True)
    bedrooms = BedroomSerializer(read_only=True, many=True)
    services = ServiceSerializer(read_only=True, many=True)

    class Meta:
        model = Hotel
        fields = "__all__"
        read_only_fields = ['reviews', 'promotions']
