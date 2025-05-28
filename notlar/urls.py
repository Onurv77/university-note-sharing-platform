from django.urls import path
from .views import not_list, not_ekle, yorum_ekle, like_not, not_detay, not_sil


urlpatterns = [
    path('', not_list, name='not_list'),
    path('ekle/', not_ekle, name='not_ekle'),
    path('<int:not_id>/yorum-ekle/', yorum_ekle, name='yorum_ekle'),
    path('<int:not_id>/like/', like_not, name='like_not'),
    path("<int:not_id>/", not_detay, name="not_detay"),  # Not detayına yönlendirme
    path('<int:not_id>/sil/', not_sil, name='not_sil'),  # Not silme URL’si eklendi

]