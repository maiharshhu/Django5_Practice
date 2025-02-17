from django.shortcuts import render
from student.forms import Registration, Login
# Create your views here.


def registration(req):
    # fm = Registration()
    fm = Registration(field_order=['email', 'city'])
    return render(req, 'student/registration.html', {'form': fm})


def login(req):
    # fm = Login(auto_id='sonam_%s')
    # fm = Login(auto_id=True)
    # fm = Login(auto_id=False)
    # fm = Login(auto_id='harsh')  # same as true

    # fm = Login(label_suffix='A')
    # fm = Login(label_suffix=' ')

    fm = Login(initial={'email': 'sonam@example.com', 'password': '1234'})

    return render(req, 'student/login.html', {'form': fm})
