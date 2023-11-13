from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="User Name")
    password = forms.CharField(label="Password",widget=forms.PasswordInput)