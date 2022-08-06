from django.urls import path
from .views import (
    GetYourProfileApiView,
    StudentsListView,
    SuccessfullApplied,
    UpdateProfileApiView,
)

urlpatterns = [
    path("all/", StudentsListView.as_view, name="all_students"),
    path("me/", GetYourProfileApiView.as_view(), name="my profile"),
    path(
        "update/<str:username>/", UpdateProfileApiView.as_view(), name="updata_profile"
    ),
    path(
        "update/status/<str:username>/",
        SuccessfullApplied.as_view(),
        name="update_profile",
    ),
]
