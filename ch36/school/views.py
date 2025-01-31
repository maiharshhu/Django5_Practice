from django.shortcuts import render
from school.forms import StudentRegistration, TeacherRegistration
# Create your views here.


def student_form_view(request):
    if request.method == 'POST':
        form = StudentRegistration(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = StudentRegistration()
    return render(request, 'school/studentreg.html',{'form':form})


def teacher_form_view(request):
    if request.method == 'POST':
        form = TeacherRegistration(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TeacherRegistration()
    return render(request, 'school/teacherreg.html',{'form':form})

