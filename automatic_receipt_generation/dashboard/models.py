from django.db import models

# Create your models here.
class SAPfile(models.Model) :
    sample_SAP = models.FileField(upload_to='SAP/')
    
    def __str__(self) :
        return 