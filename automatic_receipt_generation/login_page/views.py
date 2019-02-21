from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login_page(request) :
    return render(request, './login_page/login.html')