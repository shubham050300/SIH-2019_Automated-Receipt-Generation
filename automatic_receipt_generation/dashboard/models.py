from django.db import models

# Create your models here.
class SAPfile(models.Model) :
    Cheque_SAP = models.FileField(upload_to='SAP/')
    Card_SAP = models.FileField(upload_to='SAP/')
    OCR_image = models.ImageField(upload_to='OCR/')
    desc = models.CharField(max_length = 1024, default = 'SAP file')
    
    def __str__(self) :
        return self.desc
