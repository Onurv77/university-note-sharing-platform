from django.contrib import admin
from .models import Not, Yorum



class NotAdmin(admin.ModelAdmin):
    #list_display = ('id', 'title', 'user', 'is_approved', 'created_at')
    #list_filter = ('is_approved',)  # Admin panelinde filtreleme ekleyelim
    actions = ['approve_notlar']

    def approve_notlar(self, request, queryset):
        queryset.update(is_approved=True)
    approve_notlar.short_description = "Seçilen notları onayla"




class YorumAdmin(admin.ModelAdmin):
    list_display = ('id', 'not_obj', 'user', 'created_at', 'text')  # ID'yi burada da ekledik

admin.site.register(Not, NotAdmin)
admin.site.register(Yorum, YorumAdmin)