from django.db import models
from django.contrib.auth.models import User




class Not(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='notlar/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)  # Moderasyon için onay alanı

    def __str__(self):
        return self.title

    
class Yorum(models.Model):
    not_obj = models.ForeignKey(Not, on_delete=models.CASCADE, related_name="yorumlar")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.text[:50]}"

class Like(models.Model):
    not_obj = models.ForeignKey(Not, on_delete=models.CASCADE, related_name="likes")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('not_obj', 'user')  # Aynı kullanıcı bir notu yalnızca bir kez beğenebilir

    def __str__(self):
        return f"{self.user.username} liked {self.not_obj.title}"