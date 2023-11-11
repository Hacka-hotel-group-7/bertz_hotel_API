from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView, ListCreateAPIView
from .models import User
from .serializers import UserSerializer
from .serializers import CustomJWTSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class LoginJWTView(TokenObtainPairView):
    serializer_class = CustomJWTSerializer


class StaffView(ListCreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserView(CreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(RetrieveUpdateDestroyAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_url_kwarg = "user_id"
