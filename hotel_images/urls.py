from django.urls import path
from .views import HotelImageView, HotelImageDetailView

urlpatterns = [
    path("image/<hotel_id>/", HotelImageView.as_view()),
    path("image/<image_id>/", HotelImageDetailView.as_view())
]
