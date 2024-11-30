from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='customer_support_dashboard'),
    path('request/<int:request_id>', views.request_detail, name='request_detail'),
    path('request/<int:request_id>/update/', views.update_request_status, name='update_request_status'),
]