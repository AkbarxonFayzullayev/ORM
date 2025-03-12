from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from configapp.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('configapp.urls')),
    # path('', index),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
