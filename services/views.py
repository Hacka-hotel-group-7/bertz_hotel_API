from rest_framework.generics import ListCreateAPIView
from .models import Service
from .serializers import ServiceSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import HaveStaffPermission


class ServiceView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [HaveStaffPermission]

    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
