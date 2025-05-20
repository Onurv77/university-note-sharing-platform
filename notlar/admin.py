from django.contrib import admin
from .models import Not, Yorum

class NotAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'created_at')  # ID'yi ve diğer bilgileri ekledik

class YorumAdmin(admin.ModelAdmin):
    list_display = ('id', 'not_obj', 'user', 'created_at', 'text')  # ID'yi burada da ekledik

admin.site.register(Not, NotAdmin)
admin.site.register(Yorum, YorumAdmin)