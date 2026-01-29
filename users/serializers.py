from rest_framework import serializers
from django.db import transaction
from .models import User, CustomerProfile, TheatreOwnerProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}


class AdminSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data, role=User.ADMIN)
        return user


class TheatreOwnerSignUpSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = TheatreOwnerProfile
        fields = ["user", "gst_number", "address"]

    def create(self, validated_data):
        with transaction.atomic():
            user_data = validated_data.pop("user")
            user = User.objects.create_user(**user_data, role=User.THEATRE_OWNER)
            profile = TheatreOwnerProfile.objects.create(user=user, **validated_data)
            return profile


class CustomerSignUpSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = CustomerProfile
        fields = ["user", "phone_number", "preferences"]

    def create(self, validated_data):
        with transaction.atomic():
            user_data = validated_data.pop("user")
            user = User.objects.create_user(**user_data, role=User.CUSTOMER)
            profile = CustomerProfile.objects.create(user=user, **validated_data)
            return profile
