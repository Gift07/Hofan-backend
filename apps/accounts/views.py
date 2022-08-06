from rest_framework import permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from uritemplate import partial

from .exceptions import NotYourProfile, ProfileNotFound
from .serializers import ProfileSerializer, UpdateProfileSerializer
from .models import Profile
from .renderers import ProfileJSONRenderer


class StudentsListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class GetYourProfileApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [ProfileJSONRenderer]

    def get(self, request):
        user = self.request.user
        user_profile = Profile.objects.get(user=user)
        serializer = ProfileSerializer(user_profile, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class UpdateProfileApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [ProfileJSONRenderer]
    serializer_class = UpdateProfileSerializer

    def patch(self, request, username):
        try:
            Profile.objects.get(user__email=username)
        except Profile.DoesNotExist:
            raise ProfileNotFound

        user_name = request.user.email

        if user_name != username:
            raise NotYourProfile

        data = request.data
        data["status"] = "Pending"
        serializer = UpdateProfileSerializer(
            instance=request.user.Profile, data=data, partial=True
        )

        serializer.is_valid()
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


class SuccessfullApplied(APIView):
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [ProfileJSONRenderer]
    serializer_class = UpdateProfileSerializer

    def patch(self, request, username):
        try:
            Profile.objects.get(user__email=username)
        except Profile.DoesNotExist:
            raise ProfileNotFound

        user_name = request.user.email

        if user_name != username:
            raise NotYourProfile

        data = request.data

        serializer = UpdateProfileSerializer(
            instance=request.user.Profile, data=data, partial=True
        )

        serializer.is_valid()
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)
