from django import forms
from .models import Product

class RegisterForm(forms.Form):
    name = forms.CharField(
        error_messages={'required':"Enter the name of the product."},
        max_length = 45, label = "Product Name"
    )
    price = forms.IntegerField(
        error_messages={'required' : "Enter the price."},
        label = "Price"
    )
    

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        price = cleaned_data.get('price')

        if not (name and price):
            self.add_error('name', "No values")
            self.add_error('price', "No values")
            
            