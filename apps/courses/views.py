from rest_framework import generics, permissions, status
from .models import Courses
from .serializers import CourseSerializer, CourseCreateSerializer
from .exception import CourseNotFound


class DiplomaCourses(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Courses.diplomaObjects.all()
    serializer_class = CourseSerializer


class CertificateCourses(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Courses.certificateObjects.all()
    serializer_class = CourseSerializer


class AddNewCourse(generics.ListAPIView):
    pass
