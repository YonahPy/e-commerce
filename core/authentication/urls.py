from django.urls import path
from .views import Register, Login, Logout, UserInformation

urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('user/', UserInformation.as_view(), name='user-information')
]