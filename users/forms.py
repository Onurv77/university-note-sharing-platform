from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class KullaniciKayitForm(forms.ModelForm):
    first_name = forms.CharField(label="Ad", required=True, widget=forms.TextInput(attrs={'placeholder': 'Adınızı girin'}))
    last_name = forms.CharField(label="Soyad", required=True, widget=forms.TextInput(attrs={'placeholder': 'Soyadınızı girin'}))
    username = forms.CharField(label="Kullanıcı Adı", required=True, widget=forms.TextInput(attrs={'placeholder': 'Kullanıcı adınızı girin'}))
    email = forms.EmailField(label="E-posta", required=True, widget=forms.EmailInput(attrs={'placeholder': 'E-posta adresinizi girin'}))
    password = forms.CharField(label="Şifre", required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Şifrenizi girin'}))
    password2 = forms.CharField(label="Şifre (Tekrar)", required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Şifrenizi tekrar girin'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")

        if password and password2 and password != password2:
            raise ValidationError("Şifreler eşleşmiyor.")

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError("Bu kullanıcı adı zaten kullanılıyor.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Bu e-posta adresi zaten kullanılıyor.")
        return email
