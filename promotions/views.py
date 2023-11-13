from rest_framework.generics import ListCreateAPIView, DestroyAPIView
from .models import Promotion
from .serializers import PromotionSerializer


class PromotionView(ListCreateAPIView):

    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer

    def perform_create(self, serializer):
        promotion = serializer.save()
        promotion.hotels.add(self.request.data['hotel'])


class PromotionDetailView(DestroyAPIView):

    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer
    lookup_url_kwarg = 'promotion_id'
