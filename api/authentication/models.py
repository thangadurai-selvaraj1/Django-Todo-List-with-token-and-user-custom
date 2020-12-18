from datetime import timedelta

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken


class UserProfileManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, gender, password=None):
        if not email:
            raise ValueError('email not there')

        email = self.normalize_email(email=email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, gender=gender)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, gender, password):
        user = self.create_user(email=email, first_name=first_name, last_name=last_name, gender=gender,
                                password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    GENDER = (('MALE', 'MALE'), ('FEMALE', 'FEMALE'))

    first_name = models.CharField(max_length=56)
    last_name = models.CharField(max_length=56)
    email = models.EmailField(max_length=256, unique=True)
    gender = models.CharField(max_length=10, choices=GENDER)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'gender']

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def token(self):
        token = RefreshToken.for_user(self)
        # token.access_token.set_exp(lifetime=timedelta(days=10))
        return str(token.access_token)
