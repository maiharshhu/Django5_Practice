from django.shortcuts import render

# Create your views here.
# def base_page(req):
#     return render(req, 'core/base.html')

def home_page(req):
    return render(req, 'core/home.html')