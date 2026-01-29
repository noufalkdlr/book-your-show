from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from .models import Genre, Movie, Actor, Language, MovieCast
from .serializers import (
    ActorSerializer,
    GenreSerializer,
    MovieCastSerializer,
    MovieListSerializer,
    MovieCreateUpdateSerializer,
    LanguageSerializer,
    MovieCastCreateUpdateSerializer,
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


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    lookup_field = "slug"

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminRole]

        return [permissions() for permissions in permission_classes]


class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    lookup_field = "slug"

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminRole]

        return [permissions() for permissions in permission_classes]


class MovieCastViewSet(viewsets.ModelViewSet):
    queryset = MovieCast.objects.all()
    serializer_class = MovieCastSerializer
    lookup_field = "slug"

    def get_queryset(self):
        slug = self.kwargs["movie_slug"]
        return MovieCast.objects.filter(movie__slug=slug)

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return MovieCastCreateUpdateSerializer
        else:
            return MovieCastSerializer

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminRole]

        return [permissions() for permissions in permission_classes]

    def perform_create(self, serializer):
        slug = self.kwargs["movie_slug"]
        movie = get_object_or_404(Movie, slug=slug)
        return serializer.save(movie=movie)
