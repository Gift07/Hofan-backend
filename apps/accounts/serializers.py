from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source="user.first_name")
    middle_name = serializers.CharField(source="user.middle_name")
    sur_name = serializers.CharField(source="user.sur_name")
    email = serializers.EmailField(source="user.email")
    gender = serializers.CharField(source="user.gender")
    phone_number = serializers.CharField(source="user.phone_number")
    staff = serializers.BooleanField(source="user.is_staff")

    class Meta:
        model = Profile
        fields = [
            "first_name",
            "middle_name",
            "sur_name",
            "email",
            "staff",
            "phone_number",
            "gender",
            "status",
            "form_four_number",
            "date_of_birth",
            "place_of_birth",
            "place_of_olevo_completion",
        ]


class UpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            "status",
            "form_four_number",
            "date_of_birth",
            "place_of_birth",
            "place_of_olevo_completion",
        ]
