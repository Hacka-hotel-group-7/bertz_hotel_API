from django.urls import path
from .views import BedroomView, BedroomDetailView

urlpatterns = [
    path("bedroom/", BedroomView.as_view()),
    path("bedroom/<bedroom_id>/", BedroomDetailView.as_view())
]
