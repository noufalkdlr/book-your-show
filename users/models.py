from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ADMIN = "admin"
    THEATRE_OWNER = "theatre_owner"
    CUSTOMER = "customer"

    ROLE_CHOICES = [
        (ADMIN, "Platform Admin"),
        (THEATRE_OWNER, "Theatre Owner"),
        (CUSTOMER, "Customer"),
    ]

    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=CUSTOMER)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email


class CustomerProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="customer_profile"
    )
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    preferences = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Customer: {self.user.email}"


class TheatreOwnerProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="theatre_owner_profile"
    )
    gst_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Owner: {self.user.email}"
