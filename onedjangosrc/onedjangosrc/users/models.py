from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import OneDjangoUserManager


class User(AbstractBaseUser, PermissionsMixin):
    # essential database columns
    email = models.EmailField(
        verbose_name='email address',
        max_length=254,
        unique=True,
    )
    is_activated = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    # extra database columns
    name = models.CharField(
        verbose_name='full name',
        max_length=100,
        blank=True
    )
    date_of_birth = models.DateField(null=True, blank=True)
    # # null is database specific, blank is form validation specific

    # Django attributes
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = OneDjangoUserManager()

    # Django properties
    @property
    def is_active(self):
        return self.is_activated

    @property
    def is_staff(self):
        return self.is_admin

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)



