from rest_framework import viewsets
from .models import Movie, Actor
from .serializers import (
    ActorSerializer,
    MovieListSerializer,
    MovieCreateUpdateSerializer,
)
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


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    lookup_field = "slug"

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminRole]

        return [permissions() for permissions in permission_classes]
