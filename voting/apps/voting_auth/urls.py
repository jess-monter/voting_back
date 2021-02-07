from django.conf.urls import url, include, re_path
from rest_auth.registration.views import VerifyEmailView


urlpatterns = [
    url(r"^rest-auth/", include("rest_auth.urls")),
    url(
        r"^rest-auth/registration/",
        include("rest_auth.registration.urls"),
        name="register",
    ),
    re_path(
        r"^account-confirm-email/",
        VerifyEmailView.as_view(),
        name="account_email_verification_sent",
    ),
    re_path(
        r"^account-confirm-email/(?P<key>[-:\w]+)/$",
        VerifyEmailView.as_view(),
        name="account_confirm_email",
    ),
    url(r"^", include("django.contrib.auth.urls")),
]
