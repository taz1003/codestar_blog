from django import forms
from .models import CollaborateRequest


class CollaborateRequest(forms.ModelForm):
    class Meta:
        model: CollaborateRequest
        fields = ('name', 'email', 'message')
