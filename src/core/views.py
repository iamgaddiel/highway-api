from django.db import models
from django.db.models import query
from django.http import request
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import serializers, status, mixins, views

from core.models import CustomUser, Profile, Verification
from core.serializer import ProfileSerializer, RegistrationSerializer, VerificationSerializer


class RegistrationView(mixins.CreateModelMixin, GenericAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegistrationSerializer

    def post(self, *args, **kwargs):
        return self.create(*args, **kwargs)

class ProfileUpdateView(mixins.UpdateModelMixin, GenericAPIView):
    serializer_class = ProfileSerializer

    def get_queryset(self):
        try:
            user_id = self.request.data.get('data')
            user = CustomUser.objects.get(id=user_id)
            return Profile.objects.get(user=user)

        except CustomUser.DoesNotExist:
            return Response({"error": "wrong user credentials"}, status=status.HTTP_400_BAD_REQUEST)
        except Profile.DoesNotExist:
            return Response({"error": "profile not found"}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class VerificationView(mixins.CreateModelMixin, GenericAPIView):
    queryset = Verification.objects.all()
    serializer_class = VerificationSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)