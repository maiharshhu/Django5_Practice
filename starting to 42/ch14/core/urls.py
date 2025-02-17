from django.urls import path
from core.views import home_page


urlpatterns = [
    path('hm/', home_page),
]

