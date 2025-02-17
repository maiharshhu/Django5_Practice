from django.urls import path
from course.views import learn_python, learn_django, home


urlpatterns = [
    path('py/', learn_python, name='python'),
    path('dj/', learn_django, name='django'),
]
