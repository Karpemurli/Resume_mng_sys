from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('user/', include(('myapp.urls', 'myapp'), namespace='myapp')),

]

# Serve static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Always serve media files (some prefer restricting this to DEBUG too)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
