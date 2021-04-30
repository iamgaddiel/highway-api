from django.db.models.lookups import Lookup
from django.db.models.query import RawQuerySet
from django.shortcuts import render
from rest_framework import request, serializers, views, mixins, viewsets, status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from core.models import CustomUser

from package.models import Package, PackageLocation
from package.serializer import PackageSerializer, SingleUserPackageSerializer, UserUpdatePackageSerializer


class PackageView(viewsets.ModelViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer

class UserPackage(
    mixins.UpdateModelMixin, 
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    GenericAPIView
):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    lookup_field = "id"

    def get(self, request, *args, **kwargs):
        """kwargs: user_id"""
        return self.retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        """kwargs: user_id, id"""
        return self.update(request, *args, **kwargs)
        

class UserPackageList(views.APIView):
    def get(self, user_id, *args, **kwargs):
        try:
            user: CustomUser = CustomUser.objects.get(id=user_id)
            pckg: Package = Package.objects.filter(user=user)
            serializer = PackageSerializer(pckg, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

class GetPackageLocation(viewsets.ModelViewSet):
    serializer_class  = ""
    queryset = PackageLocation.objects.all()
    lookup_field = "id"
    