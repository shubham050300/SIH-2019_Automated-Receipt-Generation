from django.contrib import admin
from .models import Cheque_Transactions, Card_Transactions
# Register your models here.

admin.site.register(Cheque_Transactions)
admin.site.register(Card_Transactions)