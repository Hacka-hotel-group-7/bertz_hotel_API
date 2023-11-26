from rest_framework.generics import ListCreateAPIView, UpdateAPIView
from .models import Bedroom
from .serializers import BedroomSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import HasSuperuserPermission


class BedroomView(ListCreateAPIView):

    queryset = Bedroom.objects.all()
    serializer_class = BedroomSerializer
    lookup_url_kwarg = "hotel_id"

    def perform_create(self, serializer):
        serializer.save(hotel_id=self.request.data['hotel'])


class BedroomDetailView(UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [HasSuperuserPermission]

    queryset = Bedroom.objects.all()
    serializer_class = BedroomSerializer
    lookup_url_kwarg = "bedroom_id"
