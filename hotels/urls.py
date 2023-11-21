from django.urls import path
from .views import HotelView, HotelDetailView

urlpatterns = [
    path("hotel/", HotelView.as_view()),
    path("hotel/<hotel_id>/", HotelDetailView.as_view())
]
