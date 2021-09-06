from django import forms
from testapp.models import Portal
class attendance(forms.ModelForm):
    class Meta:
        model=Portal
        fields=('name','desigination')
