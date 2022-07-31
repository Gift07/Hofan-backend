from django.contrib.auth import get_user_model
from phonenumber_field.serializerfields import PhoneNumberField
from djoser.serializers import UserCreateSerializer
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "middle_name",
            "sur_name",
            "email",
            "gender",
            "phone_number",
            "is_staff",
        ]

    def to_representation(self, instance):
        respresentation = super(UserSerializer, self).to_representation(instance)
        if instance.is_superuser:
            respresentation["admin"] = True
        return respresentation


class CreateUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = [
            "id",
            "email",
            "first_name",
            "middle_name",
            "sur_name",
            "gender",
            "phone_number",
        ]
