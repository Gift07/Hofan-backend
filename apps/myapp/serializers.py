from rest_framework import serializers
from .models import MyApplication


class ApplicationSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source="user.first_name")
    middle_name = serializers.CharField(source="user.middle_name")
    sur_name = serializers.CharField(source="user.sur_name")

    class Meta:
        model = MyApplication
        fields = [
            "first_name",
            "middle_name",
            "sur_name",
            "state",
            "results",
            "education",
            "has_olevo_certificate",
            "form_four_number",
            "region_of_residence",
            "district_of_residence",
        ]


class ApplicationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyApplication
        exclude = ["created_at"]
