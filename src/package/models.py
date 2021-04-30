from enum import auto
import uuid

from django.db import models
from django.db.models.base import Model
from django.db.models.expressions import F
from django.utils import timezone

from core.models import CustomUser, Profile


class Package(models.Model):
    STATUS_CHOICES = [
        ("passanger", "passanger"),
        ("delivery", "delivery"),
        ("driver", "driver"),
        ("shipper", "shipper"),
    ]
    id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True)
    title = models.CharField(max_length=200)
    destination = models.CharField(max_length=300, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, blank=True)
    timestamp = models.DateTimeField(auto_now=timezone.now)
    lookup = models.CharField(max_length=20, choices=STATUS_CHOICES, blank=True)
    current_city = models.CharField(max_length=40, blank=True)
    contact = models.CharField(max_length=10, blank=True)
    amount = models.FloatField(default=0.00)
    is_accepted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"title: {self.title}| owner: {self.user.username} | to: {self.contact} | verified: {self.is_accepted} | timestamp: {self.timestamp}"


class PackageLocation(models.Model):
    id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4, editable=False)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    longitude = models.CharField(max_length=13)
    latitude = models.CharField(max_length=13)
    timestamp  = models.DateTimeField(auto_now=timezone.now)


    def __str__(self) -> str:
        return f"{self.package.title} | latitude : {self.latitude} | longitude: {self.longitude} | time: {self.timestamp}"