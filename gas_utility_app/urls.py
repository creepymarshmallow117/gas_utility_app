from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('service/', include('consumer_service.urls')),
    path('support/', include('customer_support.urls')),
    path('users/', include('users.urls'))
]
