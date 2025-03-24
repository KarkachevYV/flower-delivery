# catalog/forms.py
from django import forms
from .models import Flower

class FlowerForm(forms.ModelForm):
    class Meta:
        model = Flower
        fields = ('name', 'description', 'price', 'in_stock')