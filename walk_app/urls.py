from django.urls import path
from . import views

urlpatterns = [
    path('panorama/<int:pk>/', views.panorama_detail, name='panorama_detail'),
]
