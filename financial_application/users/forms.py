from .models import Account, Bank
from django import forms



class AccountForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ['account_num', 'account_name', 'account_type', 'account_bal', 'customer_id', 'bank_name']


class BankForm(forms.ModelForm):

    class Meta:
        model = Bank
        fields = ['bank_name', 'routing_number', 'bank_phone']
