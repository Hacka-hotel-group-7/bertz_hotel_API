from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView
from .models import User
from .serializers import UserSerializer


class UserView(CreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(RetrieveUpdateDestroyAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_url_kwarg = "user_id"
