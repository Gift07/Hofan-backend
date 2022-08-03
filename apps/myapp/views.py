from rest_framework import permissions, status, generics
from rest_framework.response import Response
from .models import MyApplication
from .serializers import ApplicationCreateSerializer, ApplicationSerializer
from rest_framework.views import APIView


class FetchAppliedApplications(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ApplicationSerializer
    queryset = MyApplication.appliedObjects.all()


class FetchApprovedApplications(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ApplicationSerializer
    queryset = MyApplication.approvedObjects.all()


class CreateApplication(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        user = request.user
        data = request.data
        data["user"] = request.user.pkid
        serializer = ApplicationCreateSerializer()

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
