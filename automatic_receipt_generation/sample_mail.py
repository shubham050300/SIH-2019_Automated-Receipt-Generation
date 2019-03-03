inv = 189
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'automatic_receipt_generation.settings')
import django
django.setup()
from django.shortcuts import render
from req_receipt.models import Card_Transactions, Cheque_Transactions
from dashboard.mail import mail
import datetime

card = Card_Transactions.objects.all()
cheque = Cheque_Transactions.objects.all()

def send_sample() :
    global inv
    for i in range(5) :
        invoice = inv
        inv += 1
        vemail = card[i].Vendor_email
        typ = 'Card'
        tid = card[i].Transaction_ID
        t_amt = card[i].Total_Amount
        tax_amt = card[i].Tax_amount
        lis = [invoice, vemail, typ, tid, t_amt, tax_amt]
        mail(vemail, 'Transaction_Details', 'Hello, ', lis)

        nvoice = inv
        inv += 1
        vemail = cheque[i].Vendor_email
        typ = 'Cheque'
        tid = cheque[i].Transaction_ID
        t_amt = cheque[i].Total_Amount
        tax_amt = cheque[i].Tax_amount
        lis = [invoice, vemail, typ, tid, t_amt, tax_amt]
        mail(vemail, 'Transaction_Details', 'Hello, ', lis)

