from django.urls import path, re_path
from . import views

app_name = 'blog'
urlpatterns = [
    # /blog/
    path('', views.PostLV.as_view(), name='index'),

    # /blog/post
    path('post/', views.PostLV.as_view(), name='post_list'),

    # /blog/post/django-example(slug)
    re_path(r'^post/(?P<slug>[-\w]+)/$', views.PostDV.as_view(), name='post_detail'),

    # /blog/archive
    path('archive/', views.PostAV.as_view(), name='post_archive'),

    # /blog/archive/[year]
    path('archive/<int:year>/', views.PostYAV.as_view(), name='post_year_archive'),

    # /blog/archive/[year]/[month]/
    path('archive/<int:year>/<str:month>/', views.PostMAV.as_view(), name='post_month_archive'),

    # /blog/archive/[year]/[month]/[day]
    path('archive/<int:year>/<str:month>/<int:day>/', views.PostDAV.as_view(), name='post_day_archive'),

    # /blog/archive/today
    path('archive/today/', views.PostTAV.as_view(), name='post_today_archive'),

    # /blog/search/
    path('search/', views.SearchFormView.as_view(), name='search'),
]
