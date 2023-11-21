from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .models import Review
from .serializers import ReviewSerializer
from hotels.models import Hotel


class ReviewView(ListCreateAPIView):

    serializer_class = ReviewSerializer
    lookup_url_kwarg = "hotel_id"

    def get_queryset(self):
        reviews = Hotel.objects.get(pk=self.kwargs['hotel_id'])
        return reviews.reviews

    def perform_create(self, serializer):
        review = serializer.save()
        review.hotels.add(self.kwargs['hotel_id'])
        review.guests.add(self.request.user.id)


class ReviewDetailView(RetrieveUpdateDestroyAPIView):

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_url_kwarg = "review_id"
