from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # bookmark urls.py 
    path('bookmark/', include('bookmark.urls')), 
    # blog urls.py
    path('blog/', include('blog.urls')),
    
]
