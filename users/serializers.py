from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.password_validation import validate_password

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'nickname', 'dept', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        user = CustomUser(
            email=validated_data['email'],
            nickname=validated_data['nickname'],
            dept=validated_data.get('dept', ''),
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
