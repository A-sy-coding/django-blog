from django.urls import path
from . import views

app_name = 'photo'
urlpatterns = [
    # /photo/
    path('', views.AlbumLV.as_view(), name = 'index'),
    # /photo/album/  -> 참조 함수는 위와 같다.
    path('album/', views.AlbumLV.as_view(), name='album_list'),

    # /photo/album/99/
    path('album/<int:pk>/', views.AlbumDV.as_view(), name='album_detail'),

    # /photo/photo/99/
    path('photo/<int:pk>/', views.PhotoDV.as_view(), name='photo_detail'),
]

