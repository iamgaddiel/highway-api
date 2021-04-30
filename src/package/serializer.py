from enum import unique
from django.db import models
from django.db.models import fields
from django.utils import timezone
from rest_framework import serializers, status
from rest_framework.request import override_method
from rest_framework.response import Response
from core.models import CustomUser, Profile
from package.models import Package


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = [
            "id",
            "user",
            "title",
            "destination",
            "status",
            "lookup",
            "current_city",
            "contact",
            "amount",
            "is_accepted",
        ]


class SingleUserPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = ['user']


class UserUpdatePackageSerializer(serializers.Serializer):
    STATUS_CHOICES = [
        ("passanger", "passanger"),
        ("delivery", "delivery"),
        ("driver", "driver"),
        ("shipper", "shipper"),
    ]
    user = serializers.CharField()
    title = serializers.CharField(max_length=200)
    destination = serializers.CharField(max_length=300)
    status = serializers.CharField(max_length=20)
    lookup = serializers.CharField(max_length=20)
    current_city = serializers.CharField(max_length=40)
    contact = serializers.CharField(max_length=10)
    amount = serializers.FloatField(default=0.00)
    is_accepted = serializers.BooleanField(default=False)

    class Meta:
        fields = [
            "title",
            "destination",
            "status",
            "lookup",
            "current_city",
            "contact",
            "amount",
        ]


class GetPackageSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['longitude', 'latitude', 'package']