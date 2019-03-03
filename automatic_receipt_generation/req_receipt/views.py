from django.shortcuts import render
from .render__ import Render
from .models import Card_Transactions, Cheque_Transactions
from dashboard.mail import mail
import datetime
invoice = 100
# Create your views here.

def req_page(request) :
    global invoice
    if request.method == 'POST' :
        if request.POST.get('tid') and request.POST.get('type') :
            tid = request.POST.get('tid')
            typ = request.POST.get('type')
            if typ == 'Cheque' :
                v = Cheque_Transactions.objects.get(Transaction_ID = tid)
                vid = v.Vendor_ID
                vname = v.Vendor_Name
                vemail = v.Vendor_email
                t_amt = v.Total_Amount
                tax_amt = v.Tax_amount
                d_amt = v.Discount
                pro = v.Products
                pro = pro.split(',')
                pro_new = []
                for i in pro :
                    pro_new.append(i.split(':'))
                c = {}
                for i in pro_new :
                    c[i[0]] = i[2]
                grand = 1000 #t_amt + tax_amt - d_amt
                items = {
                    'Invoice #' : invoice,
                    'Created' : datetime.datetime.now().date(),
                }
                invoice += 1
                payee_details = {
                    'Address' : 'Some Random Address',
                    'Email' : vemail,
                } 
                payment_details  = {
                    'Method' : typ,
                    'Number' : tid,
                }
                products_details = c
                other_details = {
                    'TotalAmount' : t_amt,
                    'Tax' : tax_amt,
                    'DiscountAmount' : d_amt,
                    'GrandTotal' : grand,
                }
                params = {
                   'items' : items,
                   'payee_details' : payee_details,
                   'payment_details' : payment_details,
                   'products_details' : products_details,
                   'other_details' : other_details
                }
                lis = [invoice, vemail, typ, tid, t_amt, tax_amt]
                mail(vemail, 'Transaction_Details', 'Hello, ', lis)
                return render(request, './dashboard/sent.html')

            elif typ == 'Card':
                v = Card_Transactions.objects.get(Transaction_ID = tid)
                vid = v.Vendor_ID
                vname = v.Vendor_Name
                vemail = v.Vendor_email
                t_amt = v.Total_Amount
                tax_amt = v.Tax_amount
                d_amt = v.Discount
                pro = v.Products
                pro = pro.split(',')
                pro_new = []
                for i in pro :
                    pro_new.append(i.split(':'))
                c = {}
                for i in pro_new :
                    c[i[0]] = i[2]
                grand = 1000 #str(int(t_amt) + int(tax_amt) - int(d_amt))
                items = {
                    'Invoice #' : invoice,
                    'Created' : datetime.datetime.now().date(),
                }
                invoice += 1
                payee_details = {
                    'Address' : 'Some Random Address',
                    'Email' : vemail,
                } 
                payment_details  = {
                    'Method' : typ,
                    'Number' : tid,
                }
                products_details = c
                other_details = {
                    'TotalAmount' : t_amt,
                    'Tax' : tax_amt,
                    'DiscountAmount' : d_amt,
                    'GrandTotal' : grand,
                }
                params = {
                   'items' : items,
                   'payee_details' : payee_details,
                   'payment_details' : payment_details,
                   'products_details' : products_details,
                   'other_details' : other_details
                }
                lis = [invoice, vemail, typ, tid, t_amt, tax_amt]
                
                mail(vemail, 'Transaction_Details', 'Hello, ', lis)
                return render(request, './dashboard/sent.html')
            else :
                pass
    return render(request, 'req_receipt/req_page.html')

                