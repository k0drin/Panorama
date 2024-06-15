from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from walk_app.views import subscribe
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path("admin/", admin.site.urls),
    path("", subscribe, name="default_subscribe"),
    path("walk_app/", include("walk_app.urls")),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)