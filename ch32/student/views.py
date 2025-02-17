from django.shortcuts import render
from student.forms import Registration
from django.http import HttpResponseRedirect
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            print('Name:',name)
            print('Email:',email)
            print('password',password)
            return HttpResponseRedirect('/student/register/')
    
    else:
        form = Registration()
    return render(request,'student/register.html',{'form':form})
    