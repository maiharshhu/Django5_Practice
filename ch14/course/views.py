from django.shortcuts import render

def home(request):
    return render(request, 'course/home.html')

def learn_python(request):
    return render(request, 'course/python.html') 

def learn_django(request):
    return render(request, 'course/django.html')