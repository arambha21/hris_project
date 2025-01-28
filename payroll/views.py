from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from .models import Payroll, Deduction
from .forms import PayrollForm, DeductionForm

@login_required
@permission_required('payroll.view_payroll')
def payroll_list(request):
    payrolls = Payroll.objects.all().order_by('-pay_period_end')
    return render(request, 'payroll/payroll_list.html', {'payrolls': payrolls})

@login_required
@permission_required('payroll.add_payroll')
def payroll_create(request):
    if request.method == 'POST':
        form = PayrollForm(request.POST)
        if form.is_valid():
            payroll = form.save()
            payroll.calculate_net_pay()
            messages.success(request, 'Payroll record created successfully.')
            return redirect('payroll_detail', pk=payroll.pk)
    else:
        form = PayrollForm()
    return render(request, 'payroll/payroll_form.html', {'form': form})

@login_required
@permission_required('payroll.view_payroll')
def payroll_detail(request, pk):
    payroll = get_object_or_404(Payroll, pk=pk)
    deductions = payroll.deduction_items.all()
    return render(request, 'payroll/payroll_detail.html', {'payroll': payroll, 'deductions': deductions})

@login_required
@permission_required('payroll.change_payroll')
def payroll_update(request, pk):
    payroll = get_object_or_404(Payroll, pk=pk)
    if request.method == 'POST':
        form = PayrollForm(request.POST, instance=payroll)
        if form.is_valid():
            payroll = form.save()
            payroll.calculate_net_pay()
            messages.success(request, 'Payroll record updated successfully.')
            return redirect('payroll_detail', pk=payroll.pk)
    else:
        form = PayrollForm(instance=payroll)
    return render(request, 'payroll/payroll_form.html', {'form': form, 'payroll': payroll})

@login_required
@permission_required('payroll.delete_payroll')
def payroll_delete(request, pk):
    payroll = get_object_or_404(Payroll, pk=pk)
    if request.method == 'POST':
        payroll.delete()
        messages.success(request, 'Payroll record deleted successfully.')
        return redirect('payroll_list')
    return render(request, 'payroll/payroll_confirm_delete.html', {'payroll': payroll})

@login_required
@permission_required('payroll.add_deduction')
def deduction_create(request, payroll_pk):
    payroll = get_object_or_404(Payroll, pk=payroll_pk)
    if request.method == 'POST':
        form = DeductionForm(request.POST)
        if form.is_valid():
            deduction = form.save(commit=False)
            deduction.payroll = payroll
            deduction.save()
            payroll.calculate_net_pay()
            messages.success(request, 'Deduction added successfully.')
            return redirect('payroll_detail', pk=payroll.pk)
    else:
        form = DeductionForm()
    return render(request, 'payroll/deduction_form.html', {'form': form, 'payroll': payroll})

@login_required
@permission_required('payroll.change_deduction')
def deduction_update(request, pk):
    deduction = get_object_or_404(Deduction, pk=pk)
    if request.method == 'POST':
        form = DeductionForm(request.POST, instance=deduction)
        if form.is_valid():
            form.save()
            deduction.payroll.calculate_net_pay()
            messages.success(request, 'Deduction updated successfully.')
            return redirect('payroll_detail', pk=deduction.payroll.pk)
    else:
        form = DeductionForm(instance=deduction)
    return render(request, 'payroll/deduction_form.html', {'form': form, 'deduction': deduction})

@login_required
@permission_required('payroll.delete_deduction')
def deduction_delete(request, pk):
    deduction = get_object_or_404(Deduction, pk=pk)
    payroll = deduction.payroll
    if request.method == 'POST':
        deduction.delete()
        payroll.calculate_net_pay()
        messages.success(request, 'Deduction deleted successfully.')
        return redirect('payroll_detail', pk=payroll.pk)
    return render(request, 'payroll/deduction_confirm_delete.html', {'deduction': deduction})
