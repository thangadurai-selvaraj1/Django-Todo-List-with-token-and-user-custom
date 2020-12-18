from django.contrib import admin

from api.authentication.models import UserProfile

admin.site.register(UserProfile)