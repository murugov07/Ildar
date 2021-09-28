from django import forms
from .models import SupportModel

class DataForm(forms.Form):
    error = forms.CharField(required=True)

class UserForm(forms.Form):
    name = forms.CharField(required=True)
    mail = forms.EmailField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())
    question = forms.CharField(required=True)
    answer = forms.CharField(required=True)

class QuestionForm(forms.Form):
    answer = forms.CharField(required=True)

class MailForm(forms.Form):
    mail = forms.EmailField(required=True)

class PasswordForm(forms.Form):
    password = forms.CharField(required=True, widget=forms.PasswordInput())

class SupportForm(forms.Form):
    text = forms.CharField(required=True, widget=forms.Textarea())
