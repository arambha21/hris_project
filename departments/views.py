from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from .models import Department
from .forms import DepartmentForm

@login_required
@permission_required('departments.view_department')
def department_list(request):
    departments = Department.objects.all()
    return render(request, 'departments/department_list.html', {'departments': departments})

@login_required
@permission_required('departments.view_department')
def department_detail(request, pk):
    department = get_object_or_404(Department, pk=pk)
    return render(request, 'departments/department_detail.html', {'department': department})

@login_required
@permission_required('departments.add_department')
def department_create(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            department = form.save()
            messages.success(request, 'Department created successfully.')
            return redirect('department_detail', pk=department.pk)
    else:
        form = DepartmentForm()
    return render(request, 'departments/department_form.html', {'form': form})

@login_required
@permission_required('departments.change_department')
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
    return render(request, 'departments/department_form.html', {'form': form, 'department': department})

@login_required
@permission_required('departments.delete_department')
def department_delete(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        department.delete()
        messages.success(request, 'Department deleted successfully.')
        return redirect('department_list')
    return render(request, 'departments/department_confirm_delete.html', {'department': department})
