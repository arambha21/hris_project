from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('<int:pk>/', views.employee_detail, name='employee_detail'),
    path('create/', views.employee_create, name='employee_create'),
    path('<int:pk>/update/', views.employee_update, name='employee_update'),
    path('<int:pk>/delete/', views.employee_delete, name='employee_delete'),
    path('search/', views.employee_search, name='employee_search'),
    path('<int:pk>/performance/', views.employee_performance, name='employee_performance'),
    path('<int:pk>/trainings/', views.employee_trainings, name='employee_trainings'),
    path('<int:pk>/leave-history/', views.employee_leave_history, name='employee_leave_history'),
    path('<int:pk>/payroll-history/', views.employee_payroll_history, name='employee_payroll_history'),

    # Department URLs
    path('departments/', views.department_list, name='department_list'),
    path('departments/<int:pk>/', views.department_detail, name='department_detail'),
    path('departments/create/', views.department_create, name='department_create'),
    path('departments/<int:pk>/update/', views.department_update, name='department_update'),
    path('departments/<int:pk>/delete/', views.department_delete, name='department_delete'),
]