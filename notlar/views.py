from django.shortcuts import render, redirect
from .models import Not
from .forms import NotForm
from django.contrib.auth.decorators import login_required


def not_list(request):
    notlar = Not.objects.all().order_by('-created_at')  # Yeni eklenenler en üstte olacak
    return render(request, 'notlar/not_list.html', {'notlar': notlar})

@login_required
def not_ekle(request):
    if request.method == "POST":
        form = NotForm(request.POST, request.FILES)
        if form.is_valid():
            not_obj = form.save(commit=False)
            not_obj.user = request.user  # Kullanıcıyı ilişkilendiriyoruz
            not_obj.save()
            return redirect('not_list')  # Başarıyla ekledikten sonra listeye yönlendiriyoruz
    else:
        form = NotForm()
    
    return render(request, 'notlar/not_ekle.html', {'form': form})
