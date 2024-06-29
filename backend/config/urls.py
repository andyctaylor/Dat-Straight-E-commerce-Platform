from django.contrib import admin
from django.urls import path, include

# Import settings for static files
from django.conf import settings
from django.conf.urls.static import static

# Route to the admin site amd the rest_framework
urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
]

# This is the roots to access the static files. This is only for development!
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
