from django.shortcuts import render
from student.forms import Registration
from django.http import HttpResponseRedirect
from student.models import Profile

# Create your views here.

# def register(request):
#     if request.method == 'POST':
#         form = Registration(request.POST)
#         if form.is_valid():
#             # nm = form.cleaned_data['name']
#             # em = form.cleaned_data['email']
#             # pw = form.cleaned_data['password']
#             # cpw = form.cleaned_data['password']
#             # print(f'Name:{nm}')
#             # print(f'Email:{em}')
#             # print(f'password:{pw}')
#             # print(f'confirm_password:{cpw}')
#             # Profile(name=nm, email=em, password=pw)
#             # form.save()
#             # Saving data into database
#             # syntax:- save(commit=False/True)
            
#             # Update data in database
#             # pr = Profile(id=1, name=nm, email=em, password=pw)
#             # pr.save()
            
#             # Delete Data from database
#             # pr = Profile(id=1)
#             # pr.delete()
#             return HttpResponseRedirect('/student/register/')
    
    
def register(request):
    if request.method == 'POST':
        obj = Profile.objects.get(pk=2)
        form = Registration(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/student/register/')
    
    else:
        form = Registration()
    return render(request,'student/register.html',{'form':form})    
        
        
      
