from rest_framework.generics import CreateAPIView, DestroyAPIView
from .models import Promotion
from .serializers import PromotionSerializer


class PromotionView(CreateAPIView):

    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer


class PromotionDetailView(DestroyAPIView):

    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer
