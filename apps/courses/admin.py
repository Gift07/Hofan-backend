from django.contrib import admin
from .models import Courses


class PropertyAdmin(admin.ModelAdmin):
    list_display = ["course_title", "course_years", "level"]


admin.site.register(Courses, PropertyAdmin)
