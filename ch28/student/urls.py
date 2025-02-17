from django.urls import path
from .views import registration, address, login

urlpatterns = [
    path('register/', registration, name='registration'),
    path('address/', address, name='address'),
    path('login/', login, name='login'),
]
