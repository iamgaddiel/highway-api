from django.db import models
from django.utils import timezone
import uuid
import shortuuid
from django.contrib.auth.models import User, AbstractUser


class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default = uuid.uuid4)
    phone = models.CharField(max_length=11, unique=True)

    def __str__(self) -> str:
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    # todo: make unique_code field editable=False
    unique_code = models.CharField(max_length=10, default=shortuuid.ShortUUID().random(length=9))
    state = models.CharField(max_length=20, blank=True)
    image = models.ImageField(upload_to="%Y/%m/%d-profile-images", default="user.png")
    whatsapp_number = models.CharField(max_length=11, blank=True)

    def __str__(self) -> str:
        return f"{self.user.username} profile"

class Verification(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    nin_number = models.ImageField("%Y/%m/%d-NIN-images", default="NIN.png")
    voters_card = models.ImageField("%Y/%m/%d-voter's-images", default="voters.png")
    bvn = models.CharField(max_length=12, unique=True)
    self_photo = models.ImageField(upload_to="%Y/%m/%d-verification-images", default="verification.png")
    is_verified = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=timezone.now)

    def __str__(self) -> str:
        return f"{self.user.username} verification | verified: {self.is_verified} | timeestamp : {self.timestamp}"
