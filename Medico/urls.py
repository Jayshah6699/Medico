from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('hours/', include('hours.urls')),
    path('admin/', admin.site.urls),
]
