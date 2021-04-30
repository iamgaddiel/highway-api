from django.db import models
from django.db.models import fields
from rest_framework import serializers, status
from rest_framework.response import Response
from .models import CustomUser, Profile, Verification


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(max_length=20, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'email', 'username', 'phone', 'password', 'password2']
        extra_kwargs = {
            "password": {
                "write_only": True,
                "style": {
                    "input_type": "password"
                }
            },
            "password2": {
                "write_only": True,
                "style": {
                    "input_type": "password"
                }
            },
        }

    def create(self, validated_data):
        if validated_data.pop('password') != validated_data.pop('password2'):
            return Response({"error": "passwords do not match"}, status.HTTP_400_BAD_REQUEST)
        user = CustomUser(**validated_data)
        user.set_password(validated_data.get('password'))
        user.save()
        return user

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['state', 'image', 'whatsapp_number']

class VerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Verification
        fields = ['user', 'nin_number', "voters_card", "bvn", "self_photo"]

