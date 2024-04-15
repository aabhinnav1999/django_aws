from django import forms
from app.models import customer,product

class custfm(forms.ModelForm):
    class Meta:
        model=customer
        fields='__all__'

class profm(forms.ModelForm):
    class Meta:
        model=product
        fields='__all__'