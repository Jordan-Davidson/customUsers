from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)

class SignupForm(forms.Form):
    username = forms.CharField(max_length=50)
    displayname = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)