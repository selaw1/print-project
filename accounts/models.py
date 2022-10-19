from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,PermissionsMixin)
from django.template.defaultfilters import slugify

from accounts.model_helpers import GenderChoices, make_uuid


class CustomAccountManager(BaseUserManager):
    def create_superuser(self, email, username, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, username, password, **other_fields)

    def create_user(self, email, username, password, **other_fields):

        if not email:
            raise ValueError(('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **other_fields)
        user.set_password(password)
        user.save()
        return user

class UserBase(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=make_uuid, editable=False, unique=True)
    email = models.EmailField('email address', unique=True)
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    slug = models.SlugField(max_length=150, unique=True)

    # for us only
    is_staff = models.BooleanField(default=False)
    # user status
    is_active = models.BooleanField(default=False)
    # for factories only
    is_print_factory_boss = models.BooleanField(default=False)

    # time stuff
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Custom Manager
    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'

    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.username}')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username

# class StoreProfile(models.Model):
#     id = models.UUIDField(primary_key=True, default=make_uuid, editable=False, unique=True)
#     gender = models.CharField(
#         max_length=64,
#         choices=GenderChoices.choices,
#         null=True,
#         blank=True,
#         db_index=True,
#     )
