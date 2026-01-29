from rest_framework.generics import CreateAPIView
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import (
    CustomerSignUpSerializer,
    TheatreOwnerSignUpSerializer,
    AdminSignUpSerializer,
)
from movies.permissions import IsAdminRole


class AdminSignUpView(CreateAPIView):
    serializer_class = AdminSignUpSerializer
    permission_classes = [IsAdminRole]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(
            {"message": "Admin registered successfully!", "data": response.data},
            status=status.HTTP_201_CREATED,
        )


class CustomerSignUpView(CreateAPIView):
    serializer_class = CustomerSignUpSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(
            {"message": "Customer registered successfully!", "data": response.data},
            status=status.HTTP_201_CREATED,
        )


class TheatreOwnerSignUpView(CreateAPIView):
    serializer_class = TheatreOwnerSignUpSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(
            {
                "message": "Theatre Owner registered successfully!",
                "data": response.data,
            },
            status=status.HTTP_201_CREATED,
        )
