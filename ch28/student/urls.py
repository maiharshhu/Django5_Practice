from django.urls import path
from .views import registration, address

urlpatterns = [
    path('register/', registration, name='registration'),
    path('address/', address, name='address'),
]
