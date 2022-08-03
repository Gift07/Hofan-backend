from django.urls import path
from .views import (
    CreateApplication,
    FetchAppliedApplications,
    FetchApprovedApplications,
)

urlpatterns = [
    path("applied/", FetchAppliedApplications.as_view(), name="Applied studenst"),
    path("approved/", FetchApprovedApplications.as_view(), name="Applied Students"),
    path("create/", CreateApplication.as_view(), name="Create Application"),
]
