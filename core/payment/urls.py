from django.urls import path
from .views import ValidationData
urlpatterns = [
    path('checkout/', ValidationData.as_view(), name='validation-data')
]
