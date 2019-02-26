from django.db import models

# Create your models here.
class Vendors(models.Model) :
    name = models.CharField(max_length = 264)
    vendor_id = models.CharField(max_length = 30, unique = True)

    def __str__(self) :
        return self.vendor_id

class Sent_receipts(models.Model) :
    vendor_id = models.ForeignKey(Vendors, on_delete = models.CASCADE)
    transaction_id = models.CharField(max_length = 10)
    date_time = models.DateTimeField()

    def __str__(self) :
        return self.transaction_id

class Sent_receipts_files(models.Model) :
    transaction_id = models.ForeignKey(Sent_receipts, on_delete = models.CASCADE)
    pdf_file = models.FileField()
    amount = models.CharField(max_length = 40, unique = False)

    def __str__(self) :
        return amount