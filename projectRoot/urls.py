from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('businessApp.urls')),
    path('businessApp/', include('businessApp.urls')),
    path('createUserApp/', include('createUserApp.urls')),
]
