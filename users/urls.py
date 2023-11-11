from django.urls import path
from rest_framework_simplejwt import views  # new

urlpatterns = [
    path("login/", views.TokenObtainPairView.as_view()),
]
