from django.urls import path
from .views import ServiceView

urlpatterns = [
    path("services/", ServiceView.as_view()),
]
