from django.urls import path
from .views import GetNectaResults

urlpatterns = [
    path("results/", GetNectaResults.as_view(), name="necta_results"),
]
