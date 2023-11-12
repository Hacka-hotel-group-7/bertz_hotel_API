from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from .models import Reservation
from .serializers import ReservationSerializer, ReservationSerializerUpdate
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import StaffOrOwnerPermission
from rest_framework.response import Response
from datetime import datetime


class ReservationView(ListCreateAPIView):

    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class ReservationDetailView(RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [StaffOrOwnerPermission]

    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    lookup_url_kwarg = "booking_id"

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = ReservationSerializerUpdate(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save(paid=True, checkout_date=datetime.now())

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
