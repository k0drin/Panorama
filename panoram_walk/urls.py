from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from walk_app.views import subscribe  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', subscribe, name='default_subscribe'), 
    path('walk_app/', include('walk_app.urls')),  
]
