from rest_framework.generics import ListCreateAPIView
from .models import Service
from .serializers import ServiceSerializer


class ServiceView(ListCreateAPIView):

    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
