from django.contrib import admin
from .models import Movie, Actor, Director, Genre, Language, MovieCast


admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(MovieCast)
