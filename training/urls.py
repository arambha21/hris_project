from django.urls import path
from . import views

urlpatterns = [
    path('', views.training_session_list, name='training_session_list'),
    path('create/', views.training_session_create, name='training_session_create'),
    path('<int:pk>/', views.training_session_detail, name='training_session_detail'),
    path('<int:pk>/update/', views.training_session_update, name='training_session_update'),
    path('<int:pk>/delete/', views.training_session_delete, name='training_session_delete'),
]