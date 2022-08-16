from django.urls import path
# from .views import BookmarkLV, BookmarkDV
from . import views

app_name = 'bookmark'

urlpatterns = [
    
    path('', views.BookmarkLV.as_view(), name='index'),
    path('<int:pk>/', views.BookmarkDV.as_view(), name='detail'),

    # 생성, 변경, 수전 , 삭제기능을 위한 URL
    # /bookmark/add/
    path('add/', views.BookmarkCreateView.as_view(), name='add'),
    # /bookmark/change/
    path('change/', views.BookmarkChangeLV.as_view(), name='change'),
    # /bookmark/99/update/
    path('<int:pk>/update/', views.BookmarkUpdateView.as_view(), name='update'),
    # /bookmark/99/delete/
    path('<int:pk>/delete/', views.BookmarkDeleteView.as_view(), name='delete'),
]