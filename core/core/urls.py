from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('products.urls') ),
    path('api-auth/', include('authentication.urls')),
    path('api/checkout/', include('payment.urls')),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
