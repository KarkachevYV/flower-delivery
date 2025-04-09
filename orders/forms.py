from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    comments = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "Комментарии к заказу (необязательно)"}), 
        required=False, 
        label="Комментарии"
    )

    class Meta:
        model = Order
        fields = ('status', 'comments')