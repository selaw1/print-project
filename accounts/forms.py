from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


# Custom user model
UserBase = get_user_model()

class RegistrationForm(UserCreationForm):
    class Meta:
        model = UserBase
        fields = ['username', 'email', 'first_name', 'last_name','password1', 'password2']

    def clean(self):
        print("STARTING FORM CLEANING")

        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        if username and UserBase.objects.filter(username__iexact=username).exists():
            self.add_error('username', 'A user with that username already exists.')
        
        # initial_errors = self.errors.as_data()
        return cleaned_data
