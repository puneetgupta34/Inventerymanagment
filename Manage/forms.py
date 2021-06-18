from django import forms
from .models import Product, Location, ProductMovement


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product

        fields = [
            "Product_id",
            "Quantity",
        ]


class LocationForm(forms.ModelForm):

    class Meta:
        model = Location

        fields = [
            "Location_id",
            "Address",
        ]
