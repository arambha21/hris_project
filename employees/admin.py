from django.contrib import admin
from .models import Employee, PerformanceReview, Training, LeaveRequest, Payroll, Attendance

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'get_full_name', 'department', 'position', 'hire_date')
    search_fields = ('employee_id', 'user__first_name', 'user__last_name', 'department__name', 'position')
    list_filter = ('department', 'hire_date')

@admin.register(PerformanceReview)
class PerformanceReviewAdmin(admin.ModelAdmin):
    list_display = ('employee', 'review_date', 'reviewer', 'rating')
    search_fields = ('employee__user__first_name', 'employee__user__last_name', 'reviewer__user__first_name', 'reviewer__user__last_name')
    list_filter = ('review_date', 'rating')

@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date')
    search_fields = ('name', 'description')
    filter_horizontal = ('participants',)

@admin.register(LeaveRequest)
class LeaveRequestAdmin(admin.ModelAdmin):
    list_display = ('employee', 'start_date', 'end_date', 'status')
    search_fields = ('employee__user__first_name', 'employee__user__last_name')
    list_filter = ('status', 'start_date')
@admin.register(Payroll)
class PayrollAdmin(admin.ModelAdmin):
    list_display = ('employee', 'pay_period_start', 'pay_period_end', 'net_pay')
    search_fields = ('employee__user__first_name', 'employee__user__last_name')
    list_filter = ('pay_period_start', 'pay_period_end')

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('employee', 'date', 'time_in', 'time_out')
    search_fields = ('employee__user__first_name', 'employee__user__last_name')
    list_filter = ('date',)
