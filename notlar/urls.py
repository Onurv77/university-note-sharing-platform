from django.urls import path
from .views import not_list, not_ekle

urlpatterns = [
    path('', not_list, name='not_list'),
    path('ekle/', not_ekle, name='not_ekle'),

]