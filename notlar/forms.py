from django import forms
from .models import Not

class NotForm(forms.ModelForm):
    class Meta:
        model = Not
        fields = ['title', 'description', 'file']