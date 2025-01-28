from django import forms
from .models import Payroll, Deduction

class PayrollForm(forms.ModelForm):
    class Meta:
        model = Payroll
        fields = ['employee', 'pay_period_start', 'pay_period_end', 'base_salary', 'overtime_pay', 'bonuses', 'payment_date']
        widgets = {
            'pay_period_start': forms.DateInput(attrs={'type': 'date'}),
            'pay_period_end': forms.DateInput(attrs={'type': 'date'}),
            'payment_date': forms.DateInput(attrs={'type': 'date'}),
        }

class DeductionForm(forms.ModelForm):
    class Meta:
        model = Deduction
        fields = ['name', 'description', 'amount']