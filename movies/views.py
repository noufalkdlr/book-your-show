from rest_framework import viewsets
from .models import Movie
from .serializers import MovieSerializer
from rest_framework.permissions import AllowAny


class MovieDetailView(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [AllowAny]
