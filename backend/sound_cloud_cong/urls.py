
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('oauth.urls')),
    path('api/v1/', include('sound_cloud_cong.routers')),
]
