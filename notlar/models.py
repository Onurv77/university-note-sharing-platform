from django.db import models
from django.contrib.auth.models import User

class Not(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Notu paylaşan kişi
    title = models.CharField(max_length=200)  # Notun başlığı
    description = models.TextField(blank=True)  # Açıklama
    file = models.FileField(upload_to='notlar/', blank=True, null=True)  # Dosya yükleme
    created_at = models.DateTimeField(auto_now_add=True)  # Oluşturulma zamanı

    def __str__(self):
        return self.title
    
class Yorum(models.Model):
    not_obj = models.ForeignKey(Not, on_delete=models.CASCADE, related_name="yorumlar")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.text[:50]}"
