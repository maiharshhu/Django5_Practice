from django.urls import path
from school.views import student_form_view, teacher_form_view

urlpatterns = [
    path('stu-register/',student_form_view, name="student_form_view"),
    path('tea-register/',teacher_form_view, name="teacher_form_view"),
]