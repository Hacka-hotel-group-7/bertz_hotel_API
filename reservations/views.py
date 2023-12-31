from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from .models import Reservation
from .serializers import ReservationSerializer, ReservationSerializerUpdate
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import StaffOrOwnerReservationPermission
from rest_framework.response import Response
from datetime import datetime


class ReservationView(ListCreateAPIView):

    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def perform_create(self, serializer):
        serializer.save(guest=self.request.user, bedroom_id=self.request.data['bedroom'])


class ReservationDetailView(RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [StaffOrOwnerReservationPermission]

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

        return Response({"detail": "Pagamento realizado."})
