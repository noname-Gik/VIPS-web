from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from webmain.views import *

router = DefaultRouter()

urlpatterns = [path('admin/', admin.site.urls),
               path('api/', include(router.urls)),
               path('', home, name='home'),
               ] \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
