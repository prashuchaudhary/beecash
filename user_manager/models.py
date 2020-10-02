from django.db import models
from rest_framework.authtoken.models import Token
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, Group
from user_manager.managers import AppUserManager
from utils.choice import Choice


class RoleEnum(Choice):
    ADMIN = "admin"


class User(AbstractUser):
    PHONE_REGEX = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )

    email = models.EmailField(_("email address"), null=True)
    phone = models.CharField(validators=[PHONE_REGEX], max_length=15, unique=True, db_index=True)

    objects = AppUserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['username']

    class Meta:
        ordering = ["-id"]

    def save(self, *args, **kwargs):
        created = self.pk is None
        super(User, self).save(*args, **kwargs)
        if created:
            if self.is_role_set() is False:
                self.make_admin()

    def get_auth_token(self):
        auth_token, _ = Token.objects.get_or_create(user=self)
        return auth_token.key

    @property
    def full_name(self):
        return self.get_full_name()

    @property
    def role(self):
        return self.groups.filter(user=self).first().name

    def is_role_set(self):
        return self.groups.filter(name__in=[role.value for role in RoleEnum]).exists()

    def is_admin(self):
        return self.groups.filter(name=RoleEnum.ADMIN.value).exists()

    def make_admin(self):
        admin_group = Group.objects.get(name=RoleEnum.ADMIN.value)
        self.groups.set([admin_group])
        return self

    def set_user_role(self, role):
        if role == RoleEnum.ADMIN.value:
            self.make_admin()
        else:
            raise Exception("No role like {role} found".format(role=role))
