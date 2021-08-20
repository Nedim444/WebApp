from django import forms
from .models import User, Transaction
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'