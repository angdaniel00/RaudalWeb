from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import UserAuth


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAuth
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'is_staff', 'is_superuser')


class RegisterUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAuth
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'password', 'is_staff', 'is_superuser')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        if validated_data['is_staff'] is True and validated_data['is_superuser'] is True:
            user = UserAuth.objects.create_superuser(username=validated_data['username'], email=validated_data['email'],
                                                     password=validated_data['password'],
                                                     is_staff=validated_data['is_staff'],
                                                     is_superuser=validated_data['is_superuser'],
                                                     first_name=validated_data['first_name'],
                                                     last_name=validated_data['last_name'])
        else:
            user = UserAuth.objects.create_user(username=validated_data['username'], email=validated_data['email'],
                                                password=validated_data['password'],
                                                first_name=validated_data['first_name'],
                                                last_name=validated_data['last_name'])
        return user


class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAuth
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'is_staff', 'is_superuser')


class ChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(required=False)

    class Meta:
        model = UserAuth
        fields = ('id', 'password', 'old_password')

    def update(self, instance: UserAuth, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()
        return instance


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        user = authenticate(**attrs)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Credentials incorrect')
