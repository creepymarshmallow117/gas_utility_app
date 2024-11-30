from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name='consumer_service_dashboard'),
    path('create/', views.create_service_request, name='create_request'),
    path('track/', views.track_requests, name='track_requests'),
]