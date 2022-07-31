from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class ApplicationStatus(models.TextChoices):
    INIT = "Init", _("Init")
    PENDING = "Pending", _("Pending")
    SUCCESSFUL = "Successful", _("Successful")
    REJECTED = "Rejected", _("Rejected")


class Profile(models.Model):
    user = models.OneToOneField(User, related_name="Profile", on_delete=models.CASCADE)
    status = models.CharField(
        verbose_name=_("Status"),
        max_length=30,
        choices=ApplicationStatus.choices,
        default=ApplicationStatus.INIT,
    )
    form_four_number = models.CharField(
        max_length=255, unique=True, blank=True, null=True
    )
    date_of_birth = models.DateField(null=True, blank=True)
    place_of_birth = models.CharField(
        verbose_name=_("Place of Birth"), null=True, blank=True, max_length=255
    )
    place_of_olevo_completion = models.CharField(
        verbose_name=_("Region for olevo"), max_length=255
    )

    def __str__(self):
        return self.user.sur_name
