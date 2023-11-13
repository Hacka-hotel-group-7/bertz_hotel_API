from rest_framework import serializers
from .models import Reservation
from users.serializers import UserSerializer


class ReservationSerializer(serializers.ModelSerializer):
    guest = UserSerializer(read_only=True)

    class Meta:
        model = Reservation
        fields = "__all__"
        read_only_fields = ['bedroom', 'checkout_date']
        depth = 1


class ReservationSerializerUpdate(serializers.ModelSerializer):

    class Meta:
        model = Reservation
        fields = ["payments_methods"]
