from django.db import models

# Create your models here.
class SAPfile(models.Model) :
    sample_SAP = models.FileField(upload_to='SAP/')
    desc = models.CharField(max_length = 1024, default = 'SAP file')
    
    def __str__(self) :
        return self.desc