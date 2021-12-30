from django import forms
from .models import (Category, Account, Income, Expense, )


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Account Name'}),
        }
        fields = ('name', 'currency',)


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        widgets = {}
        fields = '__all__'


class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        widgets = {
            'amount': forms.TextInput(attrs={'placeholder': 'Enter amount'}),
            'description': forms.Textarea(attrs={'placeholder': 'Tell us more', 'rows': 3, 'cols': 15})
        }
        fields = ('amount', 'category', 'account', 'description',)


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        widgets = {
            'amount': forms.TextInput(attrs={'placeholder': 'Enter amount'}),
            'description': forms.Textarea(attrs={'placeholder': 'Tell us more',
                                                 'rows': 3, 'cols': 15})
        }
        fields = ('amount', 'category', 'account', 'description',)
