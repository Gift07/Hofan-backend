from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "email",
            "first_name",
            "middle_name",
            "sur_name",
            "gender",
            "phone_number",
        ]
        error_class = "error"


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = [
            "email",
            "first_name",
            "middle_name",
            "sur_name",
            "gender",
            "phone_number",
        ]
        error_class = "error"
