from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q
from django.contrib import messages
from .models import Employee, Department
from .forms import EmployeeForm
from django.contrib.auth.models import User  # Add this line


@login_required
@permission_required('employees.view_employee')
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees/employee_list.html', {'employees': employees})

@login_required
@permission_required('employees.view_employee')
def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'employees/employee_detail.html', {'employee': employee})

@login_required
@permission_required('employees.add_employee')
def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employees/employee_form.html', {'form': form})

@login_required
@permission_required('employees.change_employee')
def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_detail', pk=employee.pk)
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employees/employee_form.html', {'form': form})

@login_required
@permission_required('employees.delete_employee')
def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'employees/employee_confirm_delete.html', {'employee': employee})

@login_required
@permission_required('employees.view_employee')
def employee_search(request):
    query = request.GET.get('q')
    if query:
        employees = Employee.objects.filter(
            Q(first_name__icontains=query) | 
            Q(last_name__icontains=query) | 
            Q(employee_id__icontains=query)
        )
    else:
        employees = Employee.objects.all()
    return render(request, 'employees/employee_list.html', {'employees': employees})

@login_required
@permission_required('employees.view_employee')
def employee_performance(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    performances = employee.performance_reviews.all()
    return render(request, 'employees/employee_performance.html', {'employee': employee, 'performances': performances})

@login_required
@permission_required('employees.view_employee')
def employee_trainings(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    trainings = employee.trainings.all()
    return render(request, 'employees/employee_trainings.html', {'employee': employee, 'trainings': trainings})

@login_required
@permission_required('employees.view_employee')
def employee_leave_history(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    leave_requests = employee.leave_requests.all()
    return render(request, 'employees/employee_leave_history.html', {'employee': employee, 'leave_requests': leave_requests})

@login_required
@permission_required('employees.view_employee')
def employee_payroll_history(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    payroll_records = employee.payroll_records.all()
    return render(request, 'employees/employee_payroll_history.html', {'employee': employee, 'payroll_records': payroll_records})

# Department Management Views
@login_required
@permission_required('employees.view_department')
def department_list(request):
    departments = Department.objects.all()
    return render(request, 'employees/department_list.html', {'departments': departments})

@login_required
@permission_required('employees.view_department')
def department_detail(request, pk):
    department = get_object_or_404(Department, pk=pk)
    return render(request, 'employees/department_detail.html', {'department': department})

@login_required
@permission_required('employees.add_department')
def department_create(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            department = form.save()
            messages.success(request, 'Department created successfully.')
            return redirect('department_detail', pk=department.pk)
    else:
        form = DepartmentForm()
    return render(request, 'employees/department_form.html', {'form': form})

@login_required
@permission_required('employees.change_department')
def department_update(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            messages.success(request, 'Department updated successfully.')
            return redirect('department_detail', pk=department.pk)
    else:
        form = DepartmentForm(instance=department)
    return render(request, 'employees/department_form.html', {'form': form, 'department': department})

@login_required
@permission_required('employees.delete_department')
def department_delete(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        department.delete()
        messages.success(request, 'Department deleted successfully.')
        return redirect('department_list')
    return render(request, 'employees/department_confirm_delete.html', {'department': department})

@login_required
@permission_required('employees.view_department')
def department_search(request):
    query = request.GET.get('q')
    if query:
        departments = Department.objects.filter(
            Q(name__icontains=query) | 
            Q(description__icontains=query)
        )
    else:
        departments = Department.objects.all()
    return render(request, 'employees/department_list.html', {'departments': departments})
