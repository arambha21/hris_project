from django.urls import path
from . import views

urlpatterns = [
    path('', views.performance_review_list, name='performance_review_list'),
    path('create/', views.performance_review_create, name='performance_review_create'),
    path('<int:pk>/', views.performance_review_detail, name='performance_review_detail'),
    path('<int:pk>/update/', views.performance_review_update, name='performance_review_update'),
    path('<int:pk>/delete/', views.performance_review_delete, name='performance_review_delete'),
]