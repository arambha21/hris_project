from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from .models import LeaveRequest
from .forms import LeaveRequestForm

@login_required
def leave_request_list(request):
    if request.user.has_perm('leave.view_leaverequest'):
        leave_requests = LeaveRequest.objects.all()
    else:
        leave_requests = LeaveRequest.objects.filter(employee=request.user.employee)
    return render(request, 'leave/leave_request_list.html', {'leave_requests': leave_requests})

@login_required
def leave_request_create(request):
    if request.method == 'POST':
        form = LeaveRequestForm(request.POST)
        if form.is_valid():
            leave_request = form.save(commit=False)
            leave_request.employee = request.user.employee
            leave_request.save()
            messages.success(request, 'Leave request submitted successfully.')
            return redirect('leave_request_list')
    else:
        form = LeaveRequestForm()
    return render(request, 'leave/leave_request_form.html', {'form': form})

@login_required
def leave_request_detail(request, pk):
    leave_request = get_object_or_404(LeaveRequest, pk=pk)
    if not request.user.has_perm('leave.view_leaverequest') and leave_request.employee != request.user.employee:
        messages.error(request, 'You do not have permission to view this leave request.')
        return redirect('leave_request_list')
    return render(request, 'leave/leave_request_detail.html', {'leave_request': leave_request})

@login_required
@permission_required('leave.change_leaverequest')
def leave_request_update(request, pk):
    leave_request = get_object_or_404(LeaveRequest, pk=pk)
    if request.method == 'POST':
        form = LeaveRequestForm(request.POST, instance=leave_request)
        if form.is_valid():
            form.save()
            messages.success(request, 'Leave request updated successfully.')
            return redirect('leave_request_list')
    else:
        form = LeaveRequestForm(instance=leave_request)
    return render(request, 'leave/leave_request_form.html', {'form': form, 'leave_request': leave_request})

@login_required
@permission_required('leave.delete_leaverequest')
def leave_request_delete(request, pk):
    leave_request = get_object_or_404(LeaveRequest, pk=pk)
    if request.method == 'POST':
        leave_request.delete()
        messages.success(request, 'Leave request deleted successfully.')
        return redirect('leave_request_list')
    return render(request, 'leave/leave_request_confirm_delete.html', {'leave_request': leave_request})

@login_required
@permission_required('leave.change_leaverequest')
def leave_request_approve_reject(request, pk):
    leave_request = get_object_or_404(LeaveRequest, pk=pk)
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'approve':
            leave_request.status = 'approved'
            leave_request.approved_by = request.user.employee
            messages.success(request, 'Leave request approved successfully.')
        elif action == 'reject':
            leave_request.status = 'rejected'
            messages.success(request, 'Leave request rejected successfully.')
        leave_request.save()
        return redirect('leave_request_list')
    return render(request, 'leave/leave_request_approve_reject.html', {'leave_request': leave_request})
