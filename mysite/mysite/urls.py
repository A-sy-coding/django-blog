from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # home(main page)
    path('', views.HomeView.as_view(), name = 'home'),
    # bookmark urls.py 
    path('bookmark/', include('bookmark.urls')), 
    # blog urls.py
    path('blog/', include('blog.urls')),
    # photo urls.py
    path('photo/', include('photo.urls')),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
