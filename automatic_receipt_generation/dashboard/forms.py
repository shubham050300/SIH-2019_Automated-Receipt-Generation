from django.forms import ModelForm
from dashboard.models import SAPfile

class SAPform(ModelForm) :
    class Meta :
        model = SAPfile
        fields = "__all__"
