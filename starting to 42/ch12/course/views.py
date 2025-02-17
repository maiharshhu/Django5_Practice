from django.shortcuts import render
from datetime import datetime
# example 1
# def learn_django(req):
#     return render(req,'course/django.html', context={'name':'Django'}) #here we are passing a context variable 'name' to the template

# example 2
# def learn_django(req):
#     name = 'Django'
#     duration = '3 months'
#     seats = 10
#     course_details = {'nm':name, 'du':duration, 'st':seats}#creating a dictionary to pass to the template
#     return render(req,'course/django.html', course_details) #here we are passing a dictionary to the template

# # example 3 filter
# def learn_django(req):
#     return render(req, 'course/django.html', context={'name':'Django', 'desc':'Django is a high-level Python web framework.'})


# # example 4 date and time
# def learn_django(req):
#     d = datetime.now()
#     return render(req, 'course/django.html', context={'dt':d})

# example 5
# def learn_django(req):
#     return render(req,'course/django.html',context={'name':'True'})

# example 6 for loop
def learn_django(req):
    student ={'names':['ram','shyam','hari','sita']}
    return render(req,'course/django.html',context=student)

def learn_python(req):
    return render(req,'course/python.html')
