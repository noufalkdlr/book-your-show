from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ADMIN = "admin"
    THEATRE_OWNER = "owner"
    CUSTOMER = "customer"

    ROLE_CHOICES = [
        ("ADMIN", "Platform Admin"),
        ("THEATRE_OWNER", "Theatre Owner"),
        ("CUSTOMER", "Customer"),
    ]

    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=CUSTOMER)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email
