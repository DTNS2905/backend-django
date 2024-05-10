from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from Innovative_project.managers import UserManager


class Host(models.Model):
    name = models.CharField(max_length=100)
    hostname = models.CharField(max_length=255, unique=True)
    address = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=20, unique=True, blank=True)
    email = models.EmailField(max_length=255, unique=True, blank=True)

    def __str__(self):
        return self.name


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length=100, unique=True
    )  # Assuming username is unique
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=20, unique=True)  # Assuming phone is unique
    host = models.ForeignKey(
        Host, on_delete=models.CASCADE, default=1
    )  # Update the reference

    USERNAME_FIELD = "username"  # Use username for user login
    REQUIRED_FIELDS = ["email", "phone"]

    objects = UserManager()

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # A flag for staff accounts
    is_superuser = models.BooleanField(default=False)  # A flag for superusers

    def __str__(self):
        return self.username
