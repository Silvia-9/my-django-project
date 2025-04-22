from django import forms
from .models import Expense

CATEGORY_CHOICES = [
    ('Food', 'Food'),
    ('Transport', 'Transport'),
    ('Entertainment', 'Entertainment'),
    ('Drinks', 'Drinks'),
    ('Health', 'Health'),
    ('Utilities', 'Utilities'),
    ('Salary', 'Salary'),
    ('Clothing', 'Clothing'),  
    ('Other', 'Other'),  
]

CURRENCY_CHOICES = [
    ('GBP', 'GBP'),
    ('USD', 'USD'),
    ('EUR', 'EUR'),
    ('NT$', 'NT$'),
    ('JPY', 'JPY'),
    ('AUD', 'AUD'),
    ('CAD', 'CAD'),
    ('CNY', 'CNY'),
    ('NZD', 'NZD'),
    ('INR', 'INR'),
]

class ExpenseForm(forms.ModelForm):
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    currency = forms.ChoiceField(choices=CURRENCY_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Expense
        fields = ['category', 'description', 'currency', 'amount']
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
        }