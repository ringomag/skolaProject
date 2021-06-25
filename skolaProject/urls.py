
from django.contrib import admin
from django.urls import path, include
#za slike
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('skola.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
