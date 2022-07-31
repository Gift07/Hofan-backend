from rest_framework import serializers
from .models import Courses


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = "__all__"


class CourseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ["course_tiltle", "course_years", "level"]
