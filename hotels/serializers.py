from rest_framework import serializers
from .models import Hotel
from hotel_images.serializers import HotelImageSerializer


class HotelSerializer(serializers.ModelSerializer):
    images = HotelImageSerializer(read_only=True, many=True)

    class Meta:
        model = Hotel
        fields = "__all__"
        read_only_fields = ['services', 'reviews', 'promotions']
