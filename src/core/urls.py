from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from .views import (
    RegistrationView,
    VerificationView
)

router = DefaultRouter('')

urlpatterns = [
    path('user/registration/', RegistrationView.as_view(), name="registration"),
    path('user/verification/', VerificationView.as_view(), name="verification"),
    # path('login/'),
    # path('logout ')

    path('package/', include('package.urls'))
]

urlpatterns += router.urls
