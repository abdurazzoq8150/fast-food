from django.db import models

# Create your models here.


from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from .validators import PhoneValidator

class UserManager(BaseUserManager):
    def get_by_natural_key(self, username):
        return self.get(username__iexact=username)

    def _create_user(self, username, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)

class User(AbstractUser):
    phone = models.CharField(max_length=15, default=None, null=True)

    objects = UserManager()


class Category(models.Model):
    name = models.CharField(max_length=155)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=155)
    description = models.CharField(max_length=155)
    image = models.ImageField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField()

    def __str__(self):
        return self.name


    