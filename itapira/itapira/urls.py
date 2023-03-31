from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path{'enquete/', include('enquete.urls')},
    path('admin/', admin.site.urls),
]
