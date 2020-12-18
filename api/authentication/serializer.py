from django.contrib import auth
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed

from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=20, min_length=3, write_only=True)

    class Meta:
        model = UserProfile
        fields = ('id', 'first_name', 'last_name', 'email', 'gender', 'password')

    def validate(self, attrs):
        email = attrs.get('email', '')
        first_name = attrs.get('first_name', '')
        last_name = attrs.get('last_name', '')
        gender = attrs.get('gender', '')

        if email == '':
            raise serializers.ValidationError({'email': 'email required'})
        if first_name == '':
            raise serializers.ValidationError({'first_name': 'first_name required'})
        if last_name == '':
            raise serializers.ValidationError({'last_name': 'last_name required'})
        if gender == '':
            raise serializers.ValidationError({'gender': 'gender required'})

        return attrs

    def create(self, validated_data):
        return UserProfile.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=20, min_length=3, write_only=True)
    email = serializers.CharField(max_length=20, min_length=3)
    first_name = serializers.CharField(max_length=56, read_only=True)
    last_name = serializers.CharField(max_length=56, read_only=True)
    gender = serializers.CharField(max_length=10, read_only=True)
    token = serializers.CharField(max_length=10, read_only=True)

    class Meta:
        model = UserProfile
        fields = ['id', 'email', 'password', 'first_name', 'last_name', 'gender', 'token']

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')

        user = auth.authenticate(email=email, password=password)

        if not user:
            raise AuthenticationFailed({'error': 'email/password incorrect'})
        return user
        return super().validate(attrs)
