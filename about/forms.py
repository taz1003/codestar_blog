from .models import CollaborateRequest
from django import forms


class CollaborateForm(forms.ModelForm):
    """
    Form for submitting a collaboration request.
    Validates the name, email, and message fields.
    """
    class Meta:
        model = CollaborateRequest
        fields = ('name', 'email', 'message')
