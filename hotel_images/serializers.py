from rest_framework import serializers
from .models import HotelImage


class HotelImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = HotelImage
        fields = "__all__"
        read_only_fields = ['hotel']
