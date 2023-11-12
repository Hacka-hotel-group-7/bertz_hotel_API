from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .models import Hotel
from .serializers import HotelSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import HaveStaffPermission


class HotelView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [HaveStaffPermission]

    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class HotelDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [HaveStaffPermission]

    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    lookup_url_kwarg = "hotel_id"
