from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def email_validator(self, email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(_("Users must provide valid email"))

    def create_user(
        self,
        email,
        first_name,
        middle_name,
        sur_name,
        gender,
        phone_number,
        password,
        **extra_fields
    ):
        if not phone_number:
            raise ValueError(_("users must have phone number"))

        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("users must have email address"))

        user = self.model(
            email=email,
            first_name=first_name,
            middle_name=middle_name,
            sur_name=sur_name,
            gender=gender,
            phone_number=phone_number,
            **extra_fields
        )
        user.set_password(password)
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        user.save(using=self._db)
        return user

    def create_superuser(
        self,
        email,
        first_name,
        middle_name,
        sur_name,
        phone_number,
        gender,
        password,
        **extra_fields
    ):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superusers musthave staff equals to true"))

        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("superusers must have superuser field set to true"))

        if not password:
            raise ValueError(_("super users must have password"))

        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("Superusers must have email"))

        user = self.create_user(
            email,
            first_name,
            middle_name,
            sur_name,
            gender,
            phone_number,
            password,
            **extra_fields
        )
        user.save(using=self._db)

        return user
