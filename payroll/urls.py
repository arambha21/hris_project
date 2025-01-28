from django.urls import path
from . import views

urlpatterns = [
    path('', views.payroll_list, name='payroll_list'),
    path('create/', views.payroll_create, name='payroll_create'),
    path('<int:pk>/', views.payroll_detail, name='payroll_detail'),
    path('<int:pk>/update/', views.payroll_update, name='payroll_update'),
    path('<int:pk>/delete/', views.payroll_delete, name='payroll_delete'),
    path('<int:payroll_pk>/deduction/create/', views.deduction_create, name='deduction_create'),
    path('deduction/<int:pk>/update/', views.deduction_update, name='deduction_update'),
    path('deduction/<int:pk>/delete/', views.deduction_delete, name='deduction_delete'),
]