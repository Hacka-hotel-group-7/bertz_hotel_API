from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView, ListCreateAPIView
from .models import User
from .serializers import UserSerializer, GuestSerializer
from .serializers import CustomJWTSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import HaveStaffPermission, StaffOrOwnerPermission


class LoginJWTView(TokenObtainPairView):
    serializer_class = CustomJWTSerializer


class StaffView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [HaveStaffPermission]

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserView(CreateAPIView):

    queryset = User.objects.all()
    serializer_class = GuestSerializer


class UserDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [StaffOrOwnerPermission]

    queryset = User.objects.all()
    serializer_class = GuestSerializer
    lookup_url_kwarg = "user_id"
