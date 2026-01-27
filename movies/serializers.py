from rest_framework import serializers
from . import models


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Genre
        fields = ["id", "name", "slug"]


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Director
        fields = ["id", "name", "slug", "photo"]


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Actor
        fields = ["id", "name", "photo"]


class MovieCastSerializer(serializers.ModelSerializer):
    actor = ActorSerializer()

    class Meta:
        model = models.MovieCast
        fields = ["id", "actor", "role_name"]


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Language
        fields = ["id", "name", "slug"]


class MovieListSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    directors = DirectorSerializer(many=True)
    cast = MovieCastSerializer(source="movie_roles", many=True)
    languages = LanguageSerializer(many=True)

    class Meta:
        model = models.Movie
        fields = [
            "id",
            "title",
            "slug",
            "description",
            "directors",
            "cast",
            "genres",
            "languages",
            "duration",
            "poster",
            "trailer_url",
            "release_date",
        ]


class MovieCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Movie
        fields = [
            "id",
            "title",
            "slug",
            "description",
            "directors",
            "cast",
            "genres",
            "languages",
            "duration",
            "poster",
            "trailer_url",
            "release_date",
        ]
