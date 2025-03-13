from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('Users.urls')),
    path('auth/', include('Authentication.urls')),
    path('inventory/', include('Inventory.urls')),
]
