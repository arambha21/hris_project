from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomUserChangeForm

def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('user_profile')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def custom_logout(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out.')
    return redirect('login')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Account created for {user.username}!')
            return redirect('profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'users/profile.html', {'form': form})

@login_required
def user_profile(request):
    return render(request, 'users/profile.html', {'user': request.user})

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.utils import timezone
from datetime import timedelta
from leave.models import LeaveRequest
from performance.models import PerformanceReview
from employees.models import Employee
from django.core.exceptions import ObjectDoesNotExist

@login_required
def dashboard(request):
    user = request.user
    try:
        employee = user.employee
        next_review = PerformanceReview.objects.filter(employee=employee).order_by('review_date').first()
        # ... rest of your existing code ...
    except ObjectDoesNotExist:
        # Handle the case where the user doesn't have an associated employee
        employee = None
        next_review = None
    permissions = {
        'can_view_employees': user.has_perm('employees.view_employee'),
        'can_view_departments': user.has_perm('employees.view_department'),
        'can_view_leave': user.has_perm('leave.view_leaverequest'),
        'can_view_training': user.has_perm('training.view_training'),
        'can_view_performance': user.has_perm('performance.view_performancereview'),
        'can_view_payroll': user.has_perm('payroll.view_payroll'),
        'can_view_attendance': user.has_perm('attendance.view_attendance'),
    }

    context = {
        'permissions': permissions,
    }

    # Only fetch metrics if user has appropriate permissions
    if permissions['can_view_leave']:
        context['pending_leave_requests'] = LeaveRequest.objects.filter(status='pending').count()

    if permissions['can_view_performance']:
        next_review = PerformanceReview.objects.filter(employee=user.employee).order_by('review_date').first()
        if next_review:
            context['days_until_next_review'] = (next_review.review_date - timezone.now().date()).days

    if permissions['can_view_employees']:
        context['total_employees'] = Employee.objects.count()

    return render(request, 'users/dashboard.html', context)

@login_required
def home(request):
    return render(request, 'users/home.html', {'user': request.user})
