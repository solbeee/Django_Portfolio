from django.contrib import admin
from django.urls import path
import experiences.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('resume', experiences.views.resume, name='resume')
]
