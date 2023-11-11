from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .models import Hotel
from .serializers import HotelSerializer


class HotelView(ListCreateAPIView):

    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class HotelDetailView(RetrieveUpdateDestroyAPIView):

    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    lookup_url_kwarg = "hotel_id"
