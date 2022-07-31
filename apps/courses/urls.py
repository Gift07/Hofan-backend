from django.urls import path
from .views import DiplomaCourses, CertificateCourses, AddNewCourse

urlpatterns = [
    path("diploma/", DiplomaCourses.as_view(), name="Diploma"),
    path("certificate/", CertificateCourses.as_view(), name="Certificate"),
    path("add/", AddNewCourse.as_view(), name="add Course"),
]
