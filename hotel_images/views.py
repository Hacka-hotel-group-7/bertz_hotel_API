from rest_framework.generics import CreateAPIView, DestroyAPIView
from .models import HotelImage
from .serializers import HotelImageSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from hotels.permissions import HaveStaffPermission


class HotelImageView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [HaveStaffPermission]

    queryset = HotelImage.objects.all()
    serializer_class = HotelImageSerializer
    lookup_url_kwarg = "hotel_id"

    def perform_create(self, serializer):
        serializer.save(hotel_id=self.kwargs[self.lookup_url_kwarg])


class HotelImageDetailView(DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [HaveStaffPermission]

    queryset = HotelImage.objects.all()
    serializer_class = HotelImageSerializer
    lookup_url_kwarg = "image_id"
