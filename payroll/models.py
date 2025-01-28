from django.db import models
from employees.models import Employee

class Payroll(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='payroll_records_payroll')
    pay_period_start = models.DateField()
    pay_period_end = models.DateField()
    base_salary = models.DecimalField(max_digits=10, decimal_places=2)
    overtime_pay = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    bonuses = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    deductions = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    net_pay = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('paid', 'Paid')], default='pending')

    def __str__(self):
        return f"Payroll for {self.employee} - {self.pay_period_start} to {self.pay_period_end}"

    def calculate_net_pay(self):
        self.net_pay = self.base_salary + self.overtime_pay + self.bonuses - self.deductions
        self.save()

class Deduction(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payroll = models.ForeignKey(Payroll, on_delete=models.CASCADE, related_name='deduction_items')

    def __str__(self):
        return f"{self.name} - {self.amount}"
