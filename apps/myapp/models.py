from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()


class ApplicationState(models.TextChoices):
    APPLIED = "Applied", _("Applied")
    APPROVED = "Approved", _("Approved")
    REJECTED = "Rejected", _("Rejected")


class Results(models.Model):
    subject = models.CharField(max_length=2, verbose_name=_("Subject"))

    class Meta:
        verbose_name = "Result"
        verbose_name_plural = "Results"


class MyApplication(models.Model):
    class ApprovedManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(state="Approved")

    class AppliedManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(state="Applied")

    class EducationLevel(models.TextChoices):
        CERTIFICATE = "Certificate", _("Certificate")
        DIPLOMA = "Diploma", _("Diploma")

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("User"))
    state = models.CharField(
        max_length=50,
        choices=ApplicationState.choices,
        default=ApplicationState.APPLIED,
        verbose_name=_("Application state"),
    )
    results = models.ManyToManyField(Results)
    education = models.CharField(
        max_length=50,
        choices=EducationLevel.choices,
        default=EducationLevel.CERTIFICATE,
        verbose_name=_("Education"),
    )
    has_olevo_certificate = models.BooleanField(
        verbose_name=_("Has certificate"), default=False
    )
    form_four_Number = models.CharField(
        max_length=255, verbose_name=_("Form four Number")
    )
    region_of_residence = models.CharField(
        max_length=255, verbose_name=_("Region of Residence")
    )
    district_of_residence = models.CharField(
        max_length=255, verbose_name=_("District of Residence")
    )
    created_at = models.DateTimeField(auto_now_add=True)
    appliedObjects = AppliedManager()
    approvedObjects = ApprovedManager()

    class Meta:
        verbose_name = _("Application")
        verbose_name_plural = _("Applications")

    def __str__(self):
        return self.form_four_Number
