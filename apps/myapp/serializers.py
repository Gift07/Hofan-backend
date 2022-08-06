from rest_framework import serializers
from .models import MyApplication, Results


class ResultsSeliazer(serializers.ModelSerializer):
    class Meta:
        model = Results
        fields = "__all__"


class ApplicationSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source="user.first_name")
    middle_name = serializers.CharField(source="user.middle_name")
    sur_name = serializers.CharField(source="user.sur_name")
    results = ResultsSeliazer()

    class Meta:
        model = MyApplication
        fields = [
            "first_name",
            "middle_name",
            "sur_name",
            "state",
            "results",
            "education",
            "selected_course",
            "has_olevo_certificate",
            "form_four_Number",
            "region_of_residence",
            "district_of_residence",
            "disability",
        ]


class ApplicationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyApplication
        exclude = ["created_at"]
