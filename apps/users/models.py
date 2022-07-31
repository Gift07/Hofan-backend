import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from .managers import CustomUserManager


class Gender(models.TextChoices):
    MALE = "Male", _("Male")
    FEMALE = "Female", _("Female")


class User(AbstractBaseUser, PermissionsMixin):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    email = models.EmailField(verbose_name=_("email"), max_length=255, unique=True)
    first_name = models.CharField(verbose_name=_("firstname"), max_length=255)
    middle_name = models.CharField(verbose_name=_("middlename"), max_length=255)
    sur_name = models.CharField(verbose_name=_("surname"), max_length=255)
    phone_number = PhoneNumberField(verbose_name=_("phonenumber"))
    gender = models.CharField(
        verbose_name=_("Gender"),
        choices=Gender.choices,
        default=Gender.MALE,
        max_length=255,
    )
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = [
        "first_name",
        "middle_name",
        "sur_name",
        "phone_number",
        "gender",
    ]

    objects = CustomUserManager()

    class Meta:
        verbose_name = (_("User"),)
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.sur_name

    @property
    def get_full_name(self):
        return f"{self.first_name.title()} {self.sur_name.title()}"

    def get_short_name(self):
        return self.sur_name
