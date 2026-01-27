from rest_framework import generics
from .models import Movie
from .serializers import MovieListSerializer
from rest_framework.permissions import AllowAny


class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializer
    permission_classes = [AllowAny]
