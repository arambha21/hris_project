from django.urls import path
from . import views
urlpatterns = [
    path('', views.leave_request_list, name='leave_request_list'),
    path('create/', views.leave_request_create, name='leave_request_create'),
    path('<int:pk>/', views.leave_request_detail, name='leave_request_detail'),
    path('<int:pk>/update/', views.leave_request_update, name='leave_request_update'),
    path('<int:pk>/delete/', views.leave_request_delete, name='leave_request_delete'),
    path('<int:pk>/approve-reject/', views.leave_request_approve_reject, name='leave_request_approve_reject'),
]