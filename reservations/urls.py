from django.urls import path
from .views import ReservationView, ReservationDetailView

urlpatterns = [
    path("bookings/", ReservationView.as_view()),
    path("bookings/<booking_id>/", ReservationDetailView.as_view()),
]
