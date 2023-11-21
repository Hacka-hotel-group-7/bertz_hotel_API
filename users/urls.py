from django.urls import path
from rest_framework_simplejwt import views
from .views import UserView, UserDetailView, StaffView, LoginJWTView

urlpatterns = [
    path("login/", LoginJWTView.as_view()),
    path("users/", UserView.as_view()),
    path("users/<user_id>/", UserDetailView.as_view()),
    path("staff/", StaffView.as_view()),
]
