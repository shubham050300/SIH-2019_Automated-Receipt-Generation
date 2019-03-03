from django.shortcuts import render
from django.core.mail import EmailMessage 
import os
import sys
from dashboard.forms import SAPform
from django.core.files.storage import FileSystemStorage
base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, base)
from sample_mail import *
# Create your views here.
def sent(request) :
    send_sample()
    return render(request, './dashboard/sent.html')

def dashboard_home(request):
    if request.method == 'POST':
        SAPf = SAPform(request.POST, request.FILES)
        if SAPf.is_valid():
            SAPf.save()
    else:
        SAPf = SAPform()
    context = {'form' : SAPf}
    return render(request, './dashboard/dashboard_home.html', context = context)