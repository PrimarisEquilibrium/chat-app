from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

# Create your models here.

class CreateUserForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "login-field-input", "name": "email", "placeholder": "Email"})
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
    
    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)

        self.fields["username"].widget.attrs["class"] = "login-field-input"
        self.fields["username"].widget.attrs["name"] = "username"
        self.fields["username"].widget.attrs["placeholder"] = "Username"

        self.fields["password1"].widget.attrs["class"] = "login-field-input"
        self.fields["password1"].widget.attrs["name"] = "password1"
        self.fields["password1"].widget.attrs["placeholder"] = "Password"

        self.fields["password2"].widget.attrs["class"] = "login-field-input"
        self.fields["password2"].widget.attrs["name"] = "password2"
        self.fields["password2"].widget.attrs["placeholder"] = "Confirm Password"