from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from Innovative_project.hosts.models import Host


class UserManager(BaseUserManager):
    def create_user(self, username, email, phone, host_id, password, is_active):
        """
        Creates and saves a User with the given email, phone, host ID, and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            phone=phone,
            host_id=host_id,
            password=password,
            is_active=is_active,
        )
        user.set_password(password)
        user.save()  # Use Django's save method
        return user

    def create_superuser(self, username, email, phone, host_id, password):
        """
        Creates and saves a superuser with the given email, phone, host ID, and password.
        """
        user = self.create_user(
            username=username,
            email=email,
            phone=phone,
            host_id=host_id,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save()  # Use Django's save method
        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True)  # Assuming username is unique
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=20, unique=True)  # Assuming phone is unique
    host_id = models.ForeignKey(Host, on_delete=models.CASCADE, default=1)  # Update the reference

    USERNAME_FIELD = 'username'  # Use username for user login
    REQUIRED_FIELDS = ['email', 'phone', 'host_id']

    objects = UserManager()

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # A flag for staff accounts
    is_superuser = models.BooleanField(default=False)  # A flag for superusers

    def __str__(self):
        return self.username
