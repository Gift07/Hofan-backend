from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from nectaapi import student
from .exceptions import NectaError


class GetNectaResults(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        data = request.data

        results = student.student(
            year=data["year"],
            exam_type=data["exam_type"],
            school_number=data["school_number"],
            student_number=data["student_number"],
        )

        if results:
            return Response(results, status=status.HTTP_200_OK)
        raise NectaError
