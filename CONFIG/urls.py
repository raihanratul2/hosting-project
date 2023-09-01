
from django.contrib import admin
from django.urls import path , include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('accounts/', include('accounts.urls')),
    path('services/', include('services.urls')),
    path('blog/', include('blog.urls')),
    path('about/', include('about_us.urls')),
    path('support/', include('support.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)