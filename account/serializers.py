from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import UserAuth


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAuth
        fields = ('id', 'username', 'email')


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAuth
        fields = ('username', 'email', 'password', 'is_staff', 'is_superuser')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        if validated_data['is_staff'] is True and validated_data['is_superuser'] is True:
            user = UserAuth.objects.create_superuser(username=validated_data['username'], email=validated_data['email'], password=validated_data['password'],
                                                is_staff=validated_data['is_staff'], is_superuser=validated_data['is_superuser'])
        else:
            user = UserAuth.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        user = authenticate(**attrs)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Credentials incorrect')
