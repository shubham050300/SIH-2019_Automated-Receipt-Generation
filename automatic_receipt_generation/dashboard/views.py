from django.shortcuts import render
from django.core.mail import EmailMessage 
from dashboard.mail import mail
from dashboard.forms import SAPform
from django.core.files.storage import FileSystemStorage


# Create your views here.
def sent(request) :
    mail('theshreyansdubey@gmail.com', 'Hello', 'PFA', '/base.html')
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