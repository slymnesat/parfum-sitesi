from django.contrib import admin
from django.urls import path, include  # include fonksiyonunu eklemeyi unutma
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalog.urls')), # Ana sayfayı catalog uygulamasına yönlendiriyoruz
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)