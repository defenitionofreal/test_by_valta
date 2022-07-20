from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):

        if not email:
            raise ValueError("User must have an email")

        if not password:
            raise ValueError("User must have a password")

        user = self.model(email=self.normalize_email(email))

        user.set_password(password)
        user.is_admin = False
        user.is_staff = False
        user.is_superuser = False
        user.is_active = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        if not password:
            raise ValueError("User must have a password")

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    """ Custom User Model """
    username = None
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return f"ID: {self.id}, Email: {self.email}"

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
