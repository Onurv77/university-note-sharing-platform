from django import forms
from .models import Not, Yorum

class NotForm(forms.ModelForm):
    class Meta:
        model = Not
        fields = ['title', 'description', 'file']

class YorumForm(forms.ModelForm):
    class Meta:
        model = Yorum
        fields = ['text']
