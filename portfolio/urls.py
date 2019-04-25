from django.contrib import admin
from django.urls import path
import experiences.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('resume', experiences.views.resume, name='resume')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
