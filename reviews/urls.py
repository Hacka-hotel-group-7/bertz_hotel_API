from django.urls import path
from .views import ReviewView, ReviewDetailView

urlpatterns = [
    path("reviews/<hotel_id>/", ReviewView.as_view()),
    path("review/<review_id>/", ReviewDetailView.as_view()),
]
