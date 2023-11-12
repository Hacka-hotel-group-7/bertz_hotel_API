from rest_framework import serializers
from .models import Reservation


class ReservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reservation
        fields = "__all__"


class ReservationSerializerUpdate(serializers.ModelSerializer):

    class Meta:
        model = Reservation
        fields = ["payments_methods"]
