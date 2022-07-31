from django.urls import path
from .views import GetYourProfileApiView, StudentsListView, UpdateProfileApiView

urlpatterns = [
    path("all/", StudentsListView.as_view, name="all_students"),
    path("me/", GetYourProfileApiView.as_view(), name="my profile"),
    path(
        "update/<str:username>/", UpdateProfileApiView.as_view(), name="updata_profile"
    ),
]
