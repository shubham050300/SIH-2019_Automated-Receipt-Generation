from django.shortcuts import render
from .models import Card_Transactions, Cheque_Transactions
from dashboard.mail import mail
# Create your views here.
def req_page(request) :
    if request.method == 'POST' :
        print('ae')
        if request.POST.get('tid') and request.POST.get('type') :
            print('ij')
            tid = request.POST.get('tid')
            typ = request.POST.get('type')
            print(typ)
            print(type(typ))
            if typ == 'Cheque' :
                print('cheque')
                t = Cheque_Transactions.objects.get(Transaction_ID = tid)
                mail('theshreyansdubey@gmail.com', 'hello', 'PFA', '/base.html')

            elif typ == 'Card':
                print('card')
                t = Card_Transactions.objects.get(Transaction_ID = tid)
                mail('theshreyansdubey@gmail.com', 'hi', 'PFA', '/base.html')
            else :
                pass
            return render(request, 'req_receipt/req_page.html')
    else :
        return render(request, 'req_receipt/req_page.html')
        
            
            

                