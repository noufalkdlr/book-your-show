from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import CustomerSignUpView, TheatreOwnerSignUpView, AdminSignUpView

urlpatterns = [
    path("signup/customer/", CustomerSignUpView.as_view(), name="customer_signup"),
    path(
        "signup/theatre-owner/",
        TheatreOwnerSignUpView.as_view(),
        name="theatre_owner_signup",
    ),
    path("signup/admin/", AdminSignUpView.as_view(), name="admin_signup"),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
