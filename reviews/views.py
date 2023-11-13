from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .models import Review
from .serializers import ReviewSerializer


class ReviewView(ListCreateAPIView):

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_url_kwarg = "hotel_id"


class ReviewDetailView(RetrieveUpdateDestroyAPIView):

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_url_kwarg = "review_id"
