"""
Root URL
"""
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail import urls as wagtail_urls
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from puput import urls as puput_urls

urlpatterns = [
    # Django admin
    path('admin/', admin.site.urls),

    # Wagtail admin and document URLs
    path('cms-admin/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),

    # Your app's URLs
    path('', include('app.urls')),

    # Wagtail blog URLs (Wagtail serves pages under /blog)
    path('blog/', include(wagtail_urls)),
]

# Static and media files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
