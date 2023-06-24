from django.urls import path
from Authentication.views import (
    RegisterView,
    VerifyEmail,
    LoginAPIView,
    RequestPasswordResetEmailAPI,
    PasswordTokenCheckAPI,
    SetNewPasswordAPIView,
    LogoutView,
    UpdateProfileView,
    ChangePasswordView,
    GetUserProfileView

)
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("email-verify/", VerifyEmail.as_view(), name="email-verify"),
    path("login/", LoginAPIView.as_view(), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path(
        "request-reset-email/",
        RequestPasswordResetEmailAPI.as_view(),
        name="request-reset-email",
    ),
    path(
        "password-reset/<uidb64>/<token>/",
        PasswordTokenCheckAPI.as_view(),
        name="password-reset-confirm",
    ),
    path(
        "password-reset-complete",
        SetNewPasswordAPIView.as_view(),
        name="password-reset-complete",
    ),
    path('update_profile/<int:pk>/', UpdateProfileView.as_view(), name='auth_update_profile'),
    path('change_password/<int:pk>/', ChangePasswordView.as_view(), name='auth_change_password'),
    path('get_user/', GetUserProfileView.as_view(), name='get_user'),
    path('logout/', LogoutView.as_view(), name="logout"),
]

