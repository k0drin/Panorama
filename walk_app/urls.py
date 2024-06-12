from django.urls import path
from . import views
from django.views.generic import TemplateView
from .views import *


urlpatterns = [
    path('panorama/<int:pk>/', views.panorama_detail, name='panorama_detail'),
    path('subscription/', TemplateView.as_view(template_name="walk_app/subscription.html"), name='subscription'),
    path('subscribe/', views.subscribe, name='subscribe'),
]
