from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import CustomerSignUpView, TheatreOwnerSignUpView

urlpatterns = [
    path("signup/customer/", CustomerSignUpView.as_view(), name="customer-signup"),
    path("signup/owner/", TheatreOwnerSignUpView.as_view(), name="owner-signup"),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
