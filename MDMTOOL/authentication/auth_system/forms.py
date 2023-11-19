
from django import forms
from .models import ImportFile

class ImportForm(forms.ModelForm):
    class Meta:
        model = ImportFile
        fields = ['file']