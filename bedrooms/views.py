from rest_framework.generics import CreateAPIView, UpdateAPIView
from .models import Bedroom
from .serializers import BedroomSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication


class BedroomView(CreateAPIView):

    queryset = Bedroom.objects.all()
    serializer_class = BedroomSerializer
    lookup_url_kwarg = "hotel_id"


class BedroomDetailView(UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = []

    queryset = Bedroom.objects.all()
    serializer_class = BedroomSerializer
    lookup_url_kwarg = "bedroom_id"
