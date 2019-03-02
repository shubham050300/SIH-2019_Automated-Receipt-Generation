from django.shortcuts import render
from .models import Card_Transactions, Cheque_Transactions
from dashboard.mail import mail
# Create your views here.
def req_page(request) :
    if request.method == 'POST' :
        if request.POST.get('tid') and request.POST.get('type') :
            tid = request.POST.get('tid')
            typ = request.POST.get('type')
            if typ == 'Cheque' :
                t = Cheque_Transactions.objects.get(Transaction_ID = tid)
                mail('theshreyansdubey@gmail.com', 'hello', 'PFA', '/base.html')

            elif typ == 'Card':
                t = Card_Transactions.objects.get(Transaction_ID = tid)
                mail('theshreyansdubey@gmail.com', 'hi', 'PFA', '/base.html')
            else :
                pass
            return render(request, 'req_receipt/req_page.html')
    else :
        return render(request, 'req_receipt/req_page.html')
        
            
            

                