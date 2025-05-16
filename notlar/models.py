from django.db import models
from django.contrib.auth.models import User

class Not(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Notu paylaşan kişi
    title = models.CharField(max_length=200)  # Notun başlığı
    description = models.TextField(blank=True)  # Açıklama
    file = models.FileField(upload_to='notlar/')  # Dosya yükleme
    created_at = models.DateTimeField(auto_now_add=True)  # Oluşturulma zamanı

    def __str__(self):
        return self.title