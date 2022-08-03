from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/auth/", include("djoser.urls")),
    path("api/v1/auth/", include("djoser.urls.jwt")),
    path("api/v1/profile/", include("apps.accounts.urls")),
    path("api/v1/courses/", include("apps.courses.urls")),
    path("api/v1/necta/", include("apps.necta.urls")),
    path("api/v1/applications/", include("apps.myapp.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "University app"
admin.site.site_title = "University App Management Page"
admin.site.index_title = "University app portal"
