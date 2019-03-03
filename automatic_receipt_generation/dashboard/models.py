from django.db import models

# Create your models here.
class SAPfile(models.Model) :
    Cheque_SAP = models.FileField(upload_to='SAP/', blank = True)
    Card_SAP = models.FileField(upload_to='SAP/', blank = True)
    OCR_image = models.ImageField(upload_to='OCR/', blank = True)
    desc = models.CharField(max_length = 1024, blank = True)
    
    def __str__(self) :
        return self.desc
