from django.urls import path
from .views import not_list, not_ekle, yorum_ekle

urlpatterns = [
    path('', not_list, name='not_list'),
    path('ekle/', not_ekle, name='not_ekle'),
    path('<int:not_id>/yorum-ekle/', yorum_ekle, name='yorum_ekle'),
]