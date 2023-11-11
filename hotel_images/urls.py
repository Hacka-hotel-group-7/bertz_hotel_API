from django.urls import path
from .views import HotelImageDetail, DestroyAPIView

urlpatterns = [
    path("image/<hotel_id>/", HotelImageDetail.as_view()),
    path("image/<image_id>/", DestroyAPIView.as_view())
]
