from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('shifts.urls')),
    path('admin/', admin.site.urls),
    path('uploader/', include('uploader.urls')),
]