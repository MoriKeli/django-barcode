from django import forms
from .models import Products


class NewProductForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'type': 'text'}), help_text='Name of the product, e.g. Radio, TV, etc.')
    product_id = forms.CharField(widget=forms.TextInput(attrs={'type': 'text'}), help_text='Product id <b>MUST</b> have a max. of 6 characters')
    manufacturer_id = forms.CharField(widget=forms.TextInput(attrs={'type': 'text'}), help_text='Manufacturer id <b>MUST</b> have a max. of 7 characters')
    country_id = forms.CharField(widget=forms.TextInput(attrs={'type': 'text'}), help_text='Country id <b>MUST</b> have a max. of 1 character')

    class Meta:
        model = Products
        fields = ['name', 'product_id', 'manufacturer_id', 'country_id']