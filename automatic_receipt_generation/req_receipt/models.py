from django.db import models

# Create your models here.
class Cheque_Transactions(models.Model) :
    date = models.DateTimeField()
    Transaction_ID = models.CharField(max_length = 15)
    Vendor_ID = models.CharField(max_length = 15)
    Vendor_Name = models.CharField(max_length = 264)
    Vendor_email = models.EmailField()
    Total_Amount = models.CharField(max_length = 20)
    Products = models.CharField(max_length = 3000)
    Tax_per = models.CharField(max_length = 10)
    Tax_amount = models.CharField(max_length = 20)
    Discount_per = models.CharField(max_length = 10)
    Discount = models.CharField(max_length = 20)
    unique_key = models.CharField(max_length = 20)

    def __str__(self) :
        return self.Transaction_ID 

class Card_Transactions(models.Model) :
    date = models.DateTimeField()
    Transaction_ID = models.CharField(max_length = 15)
    Vendor_ID = models.CharField(max_length = 15)
    Vendor_Name = models.CharField(max_length = 264)
    Vendor_email = models.EmailField()
    Total_Amount = models.CharField(max_length = 20)
    Products = models.CharField(max_length = 3000)
    Tax_per = models.CharField(max_length = 10)
    Tax_amount = models.CharField(max_length = 20)
    Discount_per = models.CharField(max_length = 10)
    Discount = models.CharField(max_length = 20)
    unique_key = models.CharField(max_length = 20)

    def __str__(self) :
        return self.Transaction_ID