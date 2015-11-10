from django import forms

class UsernameForm(forms.Form):
    username = forms.CharField(label='Username', max_length=40)
    email = forms.CharField(label='Email', max_length=40)
    password = forms.CharField(widget=forms.PasswordInput)
