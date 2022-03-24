from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    def clean_password_confirm(self):
        # Get passwords values from the form fields
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')

        # Check if passwords are equal
        if password != password_confirm:
            # Raises validation error 
            raise forms.ValidationError('The password did not match')
        return password_confirm

    def clean_email(self):
        # Get value of email field
        email = self.cleaned_data.get('email')

        # Check if email aready exists
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError('Email already exists')
        return email
    
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'password_confirm'
        ]

class UserLogInForm(forms.Form):
    username = forms.CharField(max_length=250)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        user = authenticate(username=username, password=password)

        error_msg = 'The username or password is incorrect'
        if not user:
            raise forms.ValidationError(error_msg)
        else:
            if not user.check_password(password):
                raise forms.ValidationError(error_msg)
            


        return super().clean()