from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('walk_app/', include('walk_app.urls')),  
]
