from rest_framework.generics import CreateAPIView, DestroyAPIView
from .models import HotelImage
from .serializers import HotelImageSerializer


class HotelImageView(CreateAPIView):

    queryset = HotelImage.objects.all()
    serializer_class = HotelImageSerializer
    lookup_url_kwarg = "hotel_id"

    def perform_create(self, serializer):
        serializer.save(hotel_id=self.kwargs[self.lookup_url_kwarg])


class HotelImageDetailView(DestroyAPIView):

    queryset = HotelImage.objects.all()
    serializer_class = HotelImageSerializer
    lookup_url_kwarg = "image_id"
