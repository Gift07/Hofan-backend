from enum import unique
from django.db import models
from autoslug import AutoSlugField
from django.utils.translation import gettext_lazy as _


class EducationLevel(models.TextChoices):
    CERTIFICATE = "Certificate", _("Certificate")
    DIPLOMA = "Diploma", _("Diploma")


class Courses(models.Model):
    class CertificateCourses(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(level="Certificate")

    class DiplomaCourses(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(level="Diploma")

    course_title = models.CharField(max_length=255, verbose_name=_("Course name"))
    course_years = models.IntegerField()
    level = models.CharField(
        verbose_name=_("Level"),
        max_length=50,
        choices=EducationLevel.choices,
        default=EducationLevel.CERTIFICATE,
    )
    slug = AutoSlugField(populate_from="course_title", unique=True, always_update=True)

    certificateObjects = CertificateCourses()
    diplomaObjects = DiplomaCourses()

    class Meta:
        verbose_name = _("Course")
        verbose_name_plural = _("Courses")
