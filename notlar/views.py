from django.shortcuts import render, redirect, get_object_or_404
from .models import Not, Like
from .forms import NotForm, YorumForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db import models


@login_required
def not_list(request):
   notlar = Not.objects.annotate(beğeni_sayısı=models.Count('likes')).order_by('-beğeni_sayısı', '-created_at')
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

@login_required
def yorum_ekle(request, not_id):
    not_obj = get_object_or_404(Not, id=not_id)
    if request.method == "POST":
        form = YorumForm(request.POST)
        if form.is_valid():
            yorum = form.save(commit=False)
            yorum.user = request.user
            yorum.not_obj = not_obj
            yorum.save()
            return redirect('not_list')
    else:
        form = YorumForm()
    
    return render(request, 'notlar/yorum_ekle.html', {'form': form, 'not_obj': not_obj})

@login_required
def like_not(request, not_id):
    not_obj = get_object_or_404(Not, id=not_id)
    like, created = Like.objects.get_or_create(user=request.user, not_obj=not_obj)

    if not created:
        like.delete()  # Kullanıcı beğenisini kaldırabiliyor

    like_count = not_obj.likes.count()
    return JsonResponse({'like_count': like_count})
