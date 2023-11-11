from django.urls import path
from .views import UserView, UserDetailView

urlpatterns = [
    path("users/", UserView.as_view()),
    path("users/<users_id>/", UserDetailView.as_view())
]
