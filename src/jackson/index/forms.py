from django import forms
from django.forms import TextInput, EmailInput, Textarea
from django.core.validators import EmailValidator
from django.utils.translation import gettext_lazy as _


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': _('Name'), 'label': _('Name'), 'style': '', 'class': 'form-control'}))
    email = forms.CharField(validators=[EmailValidator()], widget=forms.EmailInput(attrs={'placeholder': _('Email'), 'label': _('Email'), 'style': '', 'class': 'form-control'}))
    phone = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'placeholder': _('Phone Number'), 'label': _('Phone Number'), 'style': '', 'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': _('Let us know how we can help!'), 'label': _('Message'), 'style': '', 'class': 'form-control'}))