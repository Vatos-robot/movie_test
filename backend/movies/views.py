from rest_framework import viewsets, mixins
from rest_framework.pagination import PageNumberPagination
from .models import Movie, Review
from .serializers import (
    MovieSerializer, MovieDetailSerializer,
    ReviewSerializer
)

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    pagination_class = StandardResultsSetPagination
    http_method_names = ['get', 'patch']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return MovieDetailSerializer
        return MovieSerializer

class ReviewViewSet(mixins.CreateModelMixin,
                    viewsets.GenericViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
