from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, username, email, phone, host_id, password, is_active=True):
        """
        Creates and saves a User with the given email, phone, host ID, and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

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

    def create_superuser(self, username, email, phone, password):
        """
        Creates and saves a superuser with the given email, phone, host ID, and password.
        """
        user = self.create_user(
            username=username,
            email=email,
            phone=phone,
            host_id=1,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save()  # Use Django's save method
        return user
