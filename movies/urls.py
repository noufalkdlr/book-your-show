from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import (
    LanguageViewSet,
    MovieViewSet,
    ActorViewSet,
    GenreViewSet,
    MovieCastViewSet,
)

router = DefaultRouter()

router.register(r"movies", MovieViewSet)
router.register(r"actors", ActorViewSet)
router.register(r"genres", GenreViewSet)
router.register(r"languages", LanguageViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path(
        "movies/<slug:movie_slug>/cast/",
        MovieCastViewSet.as_view({"get": "list", "post": "create"}),
        name="movie-list",
    ),
    path(
        "movies/<slug:movie_slug>/cast/<slug:slug>/",
        MovieCastViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
        name="movie-cast-detail",
    ),
]
