from django.db import models
from django.urls import path
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter

from package.views import GetPackageLocation, PackageView,  UserPackage, UserPackageList


router = DefaultRouter()
router.register('admin/', PackageView)
router.register('package/location/', GetPackageLocation)

urlpatterns = [
    path('user/', UserPackage.as_view(), name="user-package-post"),
    path('user/<user_id>/<id>/', UserPackage.as_view(), name="user-package-get"),
    path('user/<user_id>/', UserPackageList.as_view(), name="user-package-list"),
    path('user/<user_id>/<id>/', UserPackage.as_view(), name="user-package-update"),
]

urlpatterns += router.urls