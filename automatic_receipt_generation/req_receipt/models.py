from django.db import models

# Create your models here.
class Cheque_Transactions(models.Model) :
    date = models.DateTimeField()
    Transaction_ID = models.CharField(max_length = 15)
    Vendor_ID = models.CharField(max_length = 15)
    Vendor_Name = models.CharField(max_length = 264)
    Vendor_email = models.EmailField()
    Amount = models.CharField(max_length = 20)

    def __str__(self) :
        return self.Transaction_ID 

class Card_Transactions(models.Model) :
    date = models.DateTimeField()
    Transaction_ID = models.CharField(max_length = 15)
    Vendor_ID = models.CharField(max_length = 15)
    Vendor_Name = models.CharField(max_length = 264)
    Vendor_email = models.EmailField()
    Amount = models.CharField(max_length = 20)

    def __str__(self) :
        return self.Transaction_ID