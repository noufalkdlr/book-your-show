from rest_framework import generics
from rest_framework import viewsets
from .models import Movie
from .serializers import MovieListSerializer, MovieCreateUpdateSerializer
from rest_framework.permissions import AllowAny
from .permissions import IsAdminRole


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializer
    lookup_field = "slug"

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return MovieCreateUpdateSerializer
        return MovieListSerializer

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminRole]
        return [permission() for permission in permission_classes]
