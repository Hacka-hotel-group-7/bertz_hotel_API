from rest_framework import serializers
from .models import HotelImage


class HotelImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = HotelImage
        fields = "__all__"
