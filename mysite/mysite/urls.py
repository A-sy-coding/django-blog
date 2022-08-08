from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # home(main page)
    path('', views.HomeView.as_view(), name = 'home'),
    # bookmark urls.py 
    path('bookmark/', include('bookmark.urls')), 
    # blog urls.py
    path('blog/', include('blog.urls')),
    
]
