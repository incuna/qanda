from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from user_management.models.mixins import EmailUserMixin, NameUserMixin


class User(NameUserMixin, AbstractBaseUser, EmailUserMixin, PermissionsMixin):
    pass
