from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.views.decorators.csrf import csrf_protect
from .forms import KullaniciKayitForm

@csrf_protect
def register(request):
    if request.method == "POST":
        form = KullaniciKayitForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name']
            )
            login(request, user)
            return redirect('/')  # Anasayfaya yönlendir
        else:
            print(form.errors)
    else:
        form = KullaniciKayitForm()

    return render(request, 'users/register.html', {'form': form})
