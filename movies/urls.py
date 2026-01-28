from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, ActorViewSet

router = DefaultRouter()

router.register(r"movies", MovieViewSet)
router.register(r"actors", ActorViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
