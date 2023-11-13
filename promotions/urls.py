from django.urls import path
from .views import PromotionView, PromotionDetailView

urlpatterns = [
    path("discounts/", PromotionView.as_view()),
    path("discounts/<promotion_id>/", PromotionDetailView.as_view()),
]
